from FoodApp.models import Sweet,Snack,Contact,Milkshake,User,Rolereq,buy
from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Itemform(forms.ModelForm):
	class Meta:
		model = Sweet
		fields = ['Iname','Icategory','Price','Itavilability','Iimage']
		widgets = {
		"Iname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"enter item name",
			}),
		"Icategory":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"Price":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter price",
			}),
		"Itavilability":forms.Select(attrs={
			"class":"form-control my-2",

			}),
		
		}

class Snackform(forms.ModelForm):
	class Meta:
		model=Snack
		fields = ['sname','sprice','savailability','scategory','simage']
		widgets = {
		'sname':forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter snack name",
			}),
		"sprice":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter price",
			}),
		"savailability":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"scategory":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

# class Cakeform(forms.ModelForm):
# 	class Meta:
# 		model = Cake 
# 		fields = ['cname','cprice','cavailability','ccategory','cimage']
# 		widgets = {
# 		"cname":forms.TextInput(attrs={
# 			"class":"form-control my-2",
# 			"placeholder":"Enter cake name",
# 			}),
# 		"cprice":forms.NumberInput(attrs={
# 			"class":"form-control my-2",
# 			"placeholder":"Enter price name",
# 			}),
# 		"cavailability":forms.Select(attrs={
# 			"class":"form-control my-2",
# 			}),
# 		"ccategory":forms.Select(attrs={
# 			"class":"form-control my-2",
# 			}),
# 		}

class Milkform(forms.ModelForm):
	class Meta:
		model = Milkshake
		fields = ['sname','sprice','savailability','scategory','simage']
		widgets = {
		'sname':forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Milkshake name",
			}),
		"sprice":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter price",
			}),
		"savailability":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"scategory":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}



class Contactform(forms.ModelForm):
	class Meta:
		model = Contact
		fields=['name','phone','email','content']
		widgets={
		"name":forms.TextInput(attrs={
			"class":"form-control mx-2 my-2",
			"placeholder":"Enter your name",
			}),
		"phone":forms.NumberInput(attrs={
			"class":"form-control my-2 mx-2",
			"placeholder":"Enter your phone number",
			}),
		"email":forms.TextInput(attrs={
			"class":"form-control mx-2 my-2",
			"placeholder":"Enter your email",
			}),
		"content":forms.Textarea(attrs={
			"class":"form-control mx-2 my-2",
			"placeholder":"Write Something....",
			}),
		}


class UsgForm(UserCreationForm):
	password1 = forms.CharField(widget =forms.PasswordInput(attrs={
		"class":"form-control mx-2 my-2",
		"placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget =forms.PasswordInput(attrs={
		"class":"form-control mx-2 my-2",
		"placeholder":"Confirm Password",
		}))
	class Meta:
		model = User
		fields = ['username']
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2 mx-2",
			"placeholder":"Enter your name",
			}),
		}

class Rltype(forms.ModelForm):
	class Meta:
		model = Rolereq
		fields = ['uname','rltype']
		widgets = {
		# "uname":forms.TextInput(attrs={
		# 	"class":"form-control my-2 mx-2",
		# 	"readonly":True,
		# 	}),
		"rltype":forms.Select(attrs={
			"class":"form-control mx-2 my-2",
			}),
		} 

class Rlupd(forms.ModelForm):
	class Meta:
		model = Rolereq 
		fields = ["uname","rltype"]
		widgets={
		"uname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"rltype":forms.Select(attrs={
			"class":"form-control my-2",

			}),
		}


class Buyform(forms.ModelForm):
	class Meta:
		model = buy
		fields=['name','phone','email','address']
		widgets={
		"name":forms.TextInput(attrs={
			"class":"form-control mx-2 my-2",
			"placeholder":"Enter your name",
			}),
		"phone":forms.NumberInput(attrs={
			"class":"form-control my-2 mx-2",
			"placeholder":"Enter your phone number",
			}),
		"email":forms.TextInput(attrs={
			"class":"form-control mx-2 my-2",
			"placeholder":"Enter your email",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control mx-2 my-2",
			"placeholder":"Your Adress",
			}),
		}