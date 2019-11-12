from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.admin.widgets import AdminDateWidget
from tracker.models import CustomUser, Habit, Comment, Supporter



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_name', 'profile_description', 'avatar')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_name', 'profile_description', 'avatar')

class HabitForm(forms.ModelForm):
    
    class Meta:
        model = Habit
        fields = ['title', 'number_per_day', 'start_date', 'total_number']
        widgets = {
            'start_date': DatePickerInput()               
        }    
    
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment 
        fields = '__all__'
        widgets = {'log': forms.HiddenInput(), 'comment_date': forms.HiddenInput()}

class SupporterForm(forms.Form):
    new_supporter_email = forms.EmailField()
