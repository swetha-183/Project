from django.shortcuts import render
from django.http import HttpResponse
from FoodApp.forms import Itemform,Snackform,Contactform,Milkform,UsgForm,Rltype,Rlupd,Buyform
from FoodApp.models import Sweet,Snack,Contact,Milkshake,Rolereq,User,buy
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(req):
	return render(req,'app_html/home.html')

def about(req):
	return render(req,'app_html/about.html')

def contact(req):
	if req.method =="POST":
		c = Contactform(req.POST)
		c.save()
		messages.success(req,'Submitted Successfully')
		return redirect('/cnt')
	c = Contactform()
	return render(req,'app_html/contact.html',{'o':c})
@login_required
def ilist(req):
	m = Sweet.objects.filter(sid_id=req.user.id)
	if req.method == "POST":
		k=Itemform(req.POST,req.FILES)
		if k.is_valid():
			n=k.save(commit=False)
			n.sid_id=req.user.id
			n.save()
			messages.success(req,'{} Item addedd successfully'.format(n.Iname))
			return redirect('/it')
	k = Itemform()
	return render(req,'app_html/sweetlist.html',{'r':k,'a':m})
@login_required
def swup(req,m):
	w =Sweet.objects.get(id=m)

	if req.method =="POST":
		p = Itemform(req.POST,req.FILES,instance=w)
		if p.is_valid():
			p.save()
			return redirect('/it')

	p = Itemform(instance=w)
	return render(req,'app_html/sweetupdate.html',{'s':p})
@login_required
def swdlt(req,n):
	v = Sweet.objects.get(id=n)
	if req.method == "POST":
		v.delete()
		return redirect('/it')
	return render(req,'app_html/sweetdelete.html',{'t':v})
@login_required
def swviw(req,q):
	s = Sweet.objects.get(id=q)
	return render(req,'app_html/sweetview.html',{'h':s})
@login_required
def swp(req):
	x = Sweet.objects.all()
	return render(req,'app_html/sweetpage.html',{'y':x})

#SANCKS 
@login_required
def snalist(req):
	w = Snack.objects.filter(snid_id=req.user.id)
	if req.method =="POST":
		l=Snackform(req.POST,req.FILES)
		if l.is_valid():
			g=l.save(commit=False)
			g.snid_id=req.user.id
			g.save()
			messages.success(req,'{} snack added successfully'.format(g.sname))
			return redirect('/sn')
			

	l = Snackform()
	return render(req,"app_html/snacklist.html",{'h':l,'k':w})
@login_required
def supt(req,r):
	l = Snack.objects.get(id=r)
	if req.method =="POST":
		k = Snackform(req.POST,req.FILES,instance=l)
		if k.is_valid():
			k.save()
			return redirect('/sn')
	k = Snackform(instance=l)
	return render(req,"app_html/supdate.html",{'j':k})
@login_required
def sdl(req,s):
	o = Snack.objects.get(id=s)
	if req.method=="POST":
		o.delete()
		return redirect('/sn')
	return render(req,'app_html/snackdelete.html',{'k':o})
@login_required
def snvi(req,l):
	p = Snack.objects.get(id=l)
	return render(req,'app_html/snackview.html',{'h':p})
@login_required
def snl(req):
	f = Snack.objects.all()
	return render(req,"app_html/snackpage.html",{'t':f})

#Cake
# def cak(req):
# 	w = Cake.objects.all()
# 	if req.method =="POST":
# 		l=Cakeform(req.POST,req.FILES)
# 		if l.is_valid():
# 			g=l.save(commit=False)
# 			g.save()
# 			messages.success(req,'{} cake added successfully'.format(g.cname))
# 			return redirect('/ck')

# 	l = Cakeform()
# 	return render(req,'app_html/cakelist.html',{'l':l,'b':w})

# def cake(req):
# 	k = Cakeform()
# 	return render(req,"app_html/cakel.html",{'j':k})
@login_required
def milk(req):
	d = Milkshake.objects.filter(mid_id=req.user.id)
	if req.method =="POST":
		i = Milkform(req.POST,req.FILES)
		if i.is_valid():
			n = i.save(commit=False)
			n.mid_id=req.user.id
			n.save()
			messages.info(req,'{} milkshake added successfully'.format(n.sname))
			return redirect('/mi')
	i = Milkform()
	return render(req,"app_html/milkshake.html",{'g':i,'q':d})
@login_required
def miu(req,d):
	p = Milkshake.objects.get(id=d)
	if req.method=="POST":
		p = Milkform(req.POST,req.FILES,instance=p)
		p.save()
		return redirect('/mi')
	b = Milkform(instance=p)
	return render(req,'app_html/milshkupdate.html',{'t':b})
@login_required
def midl(req,j):
	s = Milkshake.objects.get(id=j)
	if req.method == "POST":
		s.delete()
		return redirect('/mi')
	return render(req,"app_html/milshkdelete.html",{'l':s})
@login_required
def milviw(req,p):
	e = Milkshake.objects.get(id=p)
	return render(req,'app_html/milshkview.html',{'t':e})
@login_required
def milke(req):
	r = Milkshake.objects.all()
	return render(req,"app_html/milpage.html",{'s':r})

def login(req):
	return render(req,'app_html/login.html')
def register(req):
	if req.method =="POST":
		d = UsgForm(req.POST)
		if d.is_valid():
			d.save()
			return redirect('/lo')

	y = UsgForm()
	return render(req,'app_html/register.html',{'r':y})

@login_required
def roletype(req):
	p = Rolereq.objects.filter(ud_id=req.user.id).count()

	if req.method == "POST":
		s = Rltype(req.POST)
		if s.is_valid():
			y=s.save(commit=False)
			y.ud_id=req.user.id
			y.uname=req.user.username
			y.save()
			return redirect('/')
			
	s = Rltype()
	return render(req,'app_html/rolereq.html',{'u':s,'c':p})
@login_required
def gveperm(req):
	u = User.objects.all()
	r = Rolereq.objects.all()
	d = {}
	for n in u:
		for m in r:
			if n.is_superuser == 1 or n.id != m.ud_id:
				continue
			else:
				d[m.id]= m.uname,m.rltype,n.role,m.id
	return render(req,'app_html/giveperm.html',{'h':d.values})

@login_required
def gvu(req,t):
	y = Rolereq.objects.get(id=t)
	d  = User.objects.get(id=y.ud_id)
	if req.method=="POST":
		n = Rlupd(req.POST,instance=y)
		if n.is_valid():
			i = n.save(commit=False)
			d.role = i.rltype
			
			i.is_checked = 1
			i.save()
			d.save()
			return redirect('/gvp')

	n = Rlupd(instance=y)

	return render(req,'app_html/gvupdate.html',{'c':n})



def addt(req):
	if req.method =="POST":
		j = Buyform(req.POST)
		if j.is_valid():
			j.save()
			messages.info(req,'your order will be delivered to this given address - CASH-ON-DELVERY')

	j = Buyform()

	return render(req,"app_html/buy_now.html",{'k':j})