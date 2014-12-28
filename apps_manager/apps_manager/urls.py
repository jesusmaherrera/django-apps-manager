from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from applications.models import Application
from rest_framework import generics

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('name', 'description',)

# ViewSets define the view behavior.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

router.register(r'applications', ApplicationViewSet)

class ServerApolicationList(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        aplications = Server.objects.filter(user=user)[0].applications
        objects
        return aplications

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apps_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url('^server_apps/$', ServerApolicationList.as_view()), #(?P<server>.+)/
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
