distance_mi = 0.5
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = False

if distance_mi == 0:
    print("False")
elif distance_mi <= 1:
    if not is_raining:
        print("True")
    else:
        print('False')
elif distance_mi > 1 and distance_mi <= 6:
    if is_raining is False and has_bike is True:
        print("True")
    else:
        print('False')
else:
    if has_car or has_ride_share_app:
        print("True")
    else:
        print('False')

    