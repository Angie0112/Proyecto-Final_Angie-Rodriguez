
from django.shortcuts import redirect, render

def view_inicio(request):
    http_response = render(
        request=request,
        template_name='blogs/index.html',
        context={
            "userIsAuthenticated": request.user.is_authenticated,
        },
    )
    return http_response



# if request.user.is_authenticated:
#     return redirect('articulos')
# else:
#     return redirect('login')