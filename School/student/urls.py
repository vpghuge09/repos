from .views import StudentApi,TeacherApi
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register("sapi",StudentApi)
router.register('tapi',TeacherApi)
urlpatterns=router.urls