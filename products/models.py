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
    name = models.CharField(max_length=100,verbose_name = 'Nguyên liệu' )
    description = models.CharField(max_length=250, blank=True,verbose_name = 'Mô tả' )
    is_available = models.BooleanField(default=True, verbose_name = 'Khả dụng' )   
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Ngày tạo' )
    modified_at = models.DateTimeField(auto_now=True, verbose_name = 'Ngày chỉnh sửa' )
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
        limit_choices_to={'is_available': True}, verbose_name='Tên nguyên liệu')
    weight = models.FloatField(null= False, verbose_name='Khối lượng')
    cost_price = models.FloatField (null = False, verbose_name='Giá nhập')
    description = models.CharField(max_length=250, blank=True, verbose_name='Mô tả')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Ngày chỉnh sửa')

  
    
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
        limit_choices_to={'is_available': True}, verbose_name='Tên nguyên liệu')
    weight = models.FloatField(null= False, verbose_name='Khối lượng')
    description = models.CharField(max_length=250, blank=True, null=True, verbose_name='Mô tả')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Ngày chỉnh sửa')

    def __str__(self):
        return self.name.name
    class Meta:
        verbose_name = 'Hao hụt Nguyên liệu'
        verbose_name_plural = 'Hao hụt Nguyên liệu'
  
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Sản phẩm') 
    unit_price = models.FloatField (null = False, verbose_name='Giá bán')
    description = models.CharField(max_length=250, blank=True, verbose_name='Mô tả')
    discount = models.FloatField(default=0, verbose_name='Giảm giá bán')
    is_available = models.BooleanField(default=True, verbose_name='Khả dụng')   
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Ngày chỉnh sửa')
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
    name = models.CharField(max_length=50,verbose_name='Tên' )
    def __str__(self):
        return f"{self.name}"