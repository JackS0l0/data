from main.models import HeaderWall
def common_data():
    return{
        'headerwall':HeaderWall.objects.all(),
    }