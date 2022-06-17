from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import CASCADE
from xml.parsers.expat import model
from django.db import models

class Director(models.Model):
    flf = models.CharField(max_length=255,verbose_name=' ФИО-директора')
    image = models.ImageField(upload_to='media/images',verbose_name='Фото директора')
    numb = models.IntegerField(verbose_name='Номер директора')
    def __str__(self) -> str:
        return self.flf
    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'  

class Zauch(models.Model):
    flf = models.CharField(max_length=255,verbose_name='ФИО-завуча')
    image = models.ImageField(upload_to='media/images',verbose_name='Фото завуча')
    numb = models.IntegerField(verbose_name='Номер завуча')
    def __str__(self) -> str:
        return self.flf
    class Meta:
        verbose_name = 'Zauch'
        verbose_name_plural = 'Zauches'   


class Students(models.Model):
    Flf = models.CharField(max_length=255,verbose_name='ФИО-ученика')
    clan_num = models.CharField(max_length=255,verbose_name='Класс ученика')
    parents = models.IntegerField(verbose_name='Номер родителей ученика')
    location = models.CharField(max_length=255,verbose_name='Место проживания ученика')
    image = models.ImageField(upload_to='media/images',verbose_name='Фото ученика')
    def __str__(self) -> str:
        return self.Flf
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Sudents'

class Teacher(models.Model):
    flf = models.CharField(max_length=255,verbose_name='ФИО-учителя')
    location = models.CharField(max_length=255)
    num = models.IntegerField(verbose_name='Номер учителя')
    image = models.ImageField(upload_to='media/images',verbose_name='Фото учителя')
    def __str__(self) -> str:
        return self.flf
    class Meta:
        verbose_name='Учитель'
        verbose_name_plural='Учителя'
    
class Clas(models.Model):
    clas_name = models.CharField(max_length=3,verbose_name='Буква класса')
    clas_num = models.IntegerField(verbose_name='Номер класса')
    clas_teacer = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='Учитель класса')
    def __str__(self) -> str:
        return self.clas_name
    class Meta:
        verbose_name='class'
        verbose_name_plural='Clases'




class School(models.Model):
    director = models.ForeignKey(Director,on_delete=models.CASCADE,verbose_name='Директор школы')
    zauch = models.ForeignKey(Zauch,on_delete=models.CASCADE,verbose_name='Завауч')
    teachers = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='Учителя')
    clas = models.ForeignKey(Clas,on_delete=models.CASCADE,verbose_name='Классы')
    students = models.ForeignKey(Students,on_delete=models.CASCADE,verbose_name='Ученики школы')
    lessons = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.lessons