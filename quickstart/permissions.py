#from rest_framework import permissions

#class BlacklistPermission(permissions.BasePermission):

    #def has_permission(self, request, view):
        #ip_addr = request.META['REMOTE_ADDR']
        #blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        #return not blacklisted