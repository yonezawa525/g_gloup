from django import forms
#from.models import User

#class UserForm(forms.ModelForm):
#    class Meta:
#        models = User
#        fields = '__all__'
#        labels = {'userNumber':'ID', 'userSta':'出席状況', 'userTxt':'コメント', 'userUp':'更新日時'} 

class LoginForm(forms.Form):
    username = forms.CharField(label='LOGIN_ID', max_length=30)
    password = forms.CharField(
            label='PASSWORD', max_length=128, widget=forms.PasswordInput())