from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	age = models.IntegerField(default=20)
	mobilenumber = models.CharField(max_length=10,null=True)
	uimg = models.ImageField(upload_to='profilepics/',default='pic1.jpg')
	t = [(1,'Guest'),(2,'Manager'),(3,'User')]
	role = models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
	f = [(2,'Manager'),(3,'User')]
	rltype= models.IntegerField(choices=f)
	is_checked=models.BooleanField(default=False)
	uname = models.CharField(max_length=60)
	ud = models.OneToOneField(User,on_delete=models.CASCADE)


class Sweet(models.Model):
	y = [('SN','snack'),('SW','sweet'),('CA','milkshake'),('DF','select item type')]
	p = [('AV','Available'),('NV','Not Available'),('SL','select availability')]

	Iname = models.CharField(max_length=50)
	Icategory = models.CharField(choices=y,default="DF",max_length=12)
	Price = models.IntegerField()
	Iimage = models.ImageField(upload_to='Itemimages/',default='pic1.jpg')
	Itavilability = models.CharField(choices=p,default="SL",max_length=20)
	sid = models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.Iname


class Snack(models.Model):
	x=[('SN','snack'),('SW','sweet'),('CA','milkshake'),('XF','select item type')]
	g = [('AV','Available'),('NV','Not Available'),('GL','select availability')]
	sname=models.CharField(max_length=30)
	scategory = models.CharField(choices=x,default="XF",max_length=15)
	sprice=models.IntegerField()
	simage = models.ImageField(upload_to='snacimages/',default='pic1.jpg')
	savailability = models.CharField(choices=g,default="GL",max_length=20)
	snid = models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.sname

# class Cake(models.Model):
# 	o=[('SN','snack'),('SW','sweet'),('CA','cake'),('XC','select item type')]
# 	k = [('AV','Available'),('NV','Not Available'),('GC','select availability')]

# 	cname = models.CharField(max_length=40)
# 	scategory = models.CharField(choices=o,default="XC",max_length=30)
# 	cprice = models.IntegerField()
# 	cimage=models.ImageField(upload_to='cakeimages/',default='pic1.jpg')
# 	cavailability = models.CharField(choices=k,default="GC",max_length=30)

class Milkshake(models.Model):
	l=[('SN','snack'),('SW','sweet'),('CA','milkshake'),('XM','select item type')]
	s = [('AV','Available'),('NV','Not Available'),('GM','select availability')]
	sname=models.CharField(max_length=30)
	scategory = models.CharField(choices=l,default="XM",max_length=15)
	sprice=models.IntegerField()
	simage = models.ImageField(upload_to='milkimages/',default='pic1.jpg')
	savailability = models.CharField(choices=s,default="GM",max_length=20)
	mid = models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.sname





class Contact(models.Model):
	name = models.CharField(max_length=50)
	phone = models.IntegerField()
	email=models.CharField(max_length=20)
	content = models.TextField()

class buy(models.Model):
	name = models.CharField(max_length=50)
	phone = models.IntegerField()
	email=models.CharField(max_length=20)
	address = models.TextField()
