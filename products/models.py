from django.db import models




# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Danh mục'
        verbose_name_plural = 'Danh mục'

    def __str__(self):
        return self.name
    
   

class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    is_available = models.BooleanField(default=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Quản lý Nguyên liệu'
        verbose_name_plural = 'Quản lý Nguyên liệu'
    
    @property
    def import_weight(self):
        weight_import = sum(im.weight for im in self.importmaterial_set.all())
        return weight_import
    @property
    def loss_weight(self):
        weight_loss = sum(loss.weight for loss in self.materialloss_set.all())
        return weight_loss 
    
   
    
 

  

class ImportMaterial(models.Model):
    name = models.ForeignKey(Material, on_delete = models.CASCADE, 
        limit_choices_to={'is_available': True})
    weight = models.FloatField(null= False)
    cost_price = models.FloatField (null = False)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.name
    @property
    def avg_cost(self):
        avg = self.cost_price/self.weight
        return avg
    
    class Meta:
        verbose_name = 'Nhập nguyên liệu'
        verbose_name_plural = 'Nhập nguyên liệu'
  
    

class MaterialLoss(models.Model):
    name = models.ForeignKey(Material, on_delete = models.CASCADE, 
        limit_choices_to={'is_available': True})
    weight = models.FloatField(null= False)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.name
    class Meta:
        verbose_name = 'Hao hụt Nguyên liệu'
        verbose_name_plural = 'Hao hụt Nguyên liệu'
  
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    unit_price = models.FloatField (null = False)
    description = models.CharField(max_length=250, blank=True)
    discount = models.FloatField(default=0)
    is_available = models.BooleanField(default=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    
    def __str__(self):
        return self.name  
    
  
    class Meta:
        verbose_name = 'Sản phẩm'
        verbose_name_plural = 'Sản phẩm'  
    


class ProductItem(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    name = models.ForeignKey(Material, on_delete=models.CASCADE) 
    weight = models.FloatField(null= False)
    description = models.CharField(max_length=250, blank=True)
    is_available = models.BooleanField(default=True) 

class ProductCost(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True) 
    cost = models.FloatField(null= False)
    description = models.CharField(max_length=250, blank=True)
    is_available = models.BooleanField(default=True) 
    


class Tag (models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"