from rest_framework import routers

from .views import ToDoListModelViewSet, \
    ToDoListCreateViewSet

router = routers.SimpleRouter()
router.register(r'todo', ToDoListModelViewSet)
router.register(r'todo-create', ToDoListCreateViewSet)

urlpatterns = router.urls
