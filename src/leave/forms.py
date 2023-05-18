from django import forms
from .models import Leave
# from .models import Comment
import datetime

class LeaveCreationForm(forms.ModelForm):
	reason = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
	class Meta:
		model = Leave
		exclude = ['employee','defaultdays','hrcomments','status','is_approved','updated','created']



	def clean_enddate(self):
		enddate = self.cleaned_data['Дата окончания']
		startdate = self.cleaned_data['Дата начала']
		today_date = datetime.date.today()

		if (startdate or enddate) < today_date:# both dates must not be in the past
			raise forms.ValidationError("Выбранные даты неверны, пожалуйста, выберите еще раз")

		elif startdate >= enddate:# TRUE -> FUTURE DATE > PAST DATE,FALSE other wise
			raise forms.ValidationError("Выбранные даты неверны")

		return enddate





# class CommentForm(forms.ModelForm):

# 	class Meta:
# 		model = Comment
# 		exclude = ['updated','created','leave']