from parking.models import ParkingSpot


def get_status_by_id(spot_id):
    p = ParkingSpot.objects.get(pk=spot_id)
    return p.status

def set_open_by_id(spot_id):
    p = ParkingSpot.objects.get(pk=spot_id)
    p.status="Open"
    p.save()
    pass

def set_taken_by_id(spot_id):
    p = ParkingSpot.objects.get(pk=spot_id)
    p.status="Taken"
    p.save()
    pass

def set_reserved_by_id(spot_id):
    p = ParkingSpot.objects.get(pk=spot_id)
    p.status="Reserved"
    p.save()
    pass