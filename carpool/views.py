from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from actions.models import Action
from .models import CarPool, regular_user
from .forms import CarpoolForm
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def login(request):
    return render(request,
                  "carpool/baseLogin.html")


def pages_home(request):
    actions = Action.objects.all().order_by('-created')

    return render(request,
                  "carpool/pages/home.html",
                  {"actions": actions}
                  )


def ride(request):
    return render(request,
                  "carpool/pages/ride.html")


def createCarpool(request):
    if request.method == 'POST':
        name = request.session['username']
        carModel = request.POST.get('Carname')
        departureTime = request.POST.get('Dtime')
        arrivalTime = request.POST.get('Atime')
        route = request.POST.get('Route')
        availableSeats = request.POST.get('Aseats')
        cp = CarPool(
            name=name,
            carModel=carModel,
            departureTime=departureTime,
            arrivalTime=arrivalTime,
            route=route,
            availableSeats=availableSeats,
        )
        cp.save()

        action = Action(
            user=name,
            verb="Carpool added by",
        )
        action.save()

        messages.add_message(request, messages.SUCCESS, "Added Carpool Successfully")
        return redirect("carpool:myCarpool")
    else:
        return render(request,
                      "carpool/pages/createCarpool.html")


def myCarpool(request):
    carpools = CarPool.objects.all()
    context = {"carpools": carpools
               }
    return render(request,
                  "carpool/pages/myCarpool.html",
                  context
                  )


def carpool_increment(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        carpool_id = request.POST.get('carpool_id')
        try:
            # Get the CarPool object by its ID
            carpool = CarPool.objects.get(id=carpool_id)
            # Increment the available seats
            carpool.availableSeats += 1
            # Save the CarPool object
            carpool.save()
            # Return a JsonResponse with success status and the new available seats
            return JsonResponse({'success': 'success', 'availableSeats': carpool.availableSeats}, status=200)
        except CarPool.DoesNotExist:
            # If the CarPool object is not found, return an error message
            return JsonResponse({'error': 'No carpool found with that ID.'}, status=400)
    else:
        # If the request is not AJAX or not a POST request, return an error message
        return JsonResponse({'error': 'Invalid Ajax request.'}, status=400)


def carpool_decrement(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        carpool_id = request.POST.get('carpool_id')
        try:
            carpool = CarPool.objects.get(pk=carpool_id)
            if carpool.availableSeats > 0:
                carpool.availableSeats -= 1
                carpool.save()
                return JsonResponse({'success': 'success', 'availableSeats': carpool.availableSeats}, status=200)
            else:
                return JsonResponse({'error': 'No more seats to decrement.'}, status=200)
        except CarPool.DoesNotExist:
            return JsonResponse({'error': 'No carpool found with that ID.'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax request.'}, status=400)


def edit_carpool(request, carpool_id):
    carpool = get_object_or_404(CarPool, id=carpool_id)
    if request.method == 'POST':
        form = CarpoolForm(request.POST, instance=carpool)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Carpool Successfully Edited")
            return redirect('carpool:myCarpool')  # Redirect to the list view or any other appropriate view
    else:
        form = CarpoolForm(instance=carpool)

    return render(request, 'carpool/pages/edit_carpool.html', {'form': form})


def delete_carpool(request, carpool_id):
    carpool = get_object_or_404(CarPool, id=carpool_id)
    if request.method == 'POST':  # Confirm deletion
        carpool.delete()
        messages.add_message(request, messages.WARNING, "Carpool Successfully Deleted")
        return redirect('carpool:myCarpool')  # Redirect to the list view or any other appropriate view
    return render(request, 'carpool/pages/confirm_delete.html', {'carpool': carpool})

def success(request):
    return render(request,
                  "carpool/pages/success.html")


def carpool_detail(request, carpool_id):
    carpools = CarPool.objects.all()
    target_carpool = None
    for carpool in carpools:
        if carpool.carpoolid == carpool_id:
            target_carpool = carpool
            break

    if target_carpool:
        return render(request, 'carpool/pages/detail.html', {'carpool': target_carpool})

# def login(request):
#     username = request.get("username")
#     pw = request.POST.get("password")
#     if(username == regular_user['username']) and (pw == regular_user['pw']):
#             redirect('carpool:pages_home')
#     else:
#         return redirect('carpool:pages_home')

# def logout(request):
#     del request.session['username']
#     del request.session['role']
#     return redirect('carpool:pages_home')