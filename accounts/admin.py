from django.contrib import admin

from accounts.models import Account


class AccountsAdmin(admin.ModelAdmin):
    field = ['email', 'gender', 'password', 'password_confirm', 'first_name', 'last_name', 'inform', 'number', 'avatar', 'birth_date']


admin.site.register(Account, AccountsAdmin)