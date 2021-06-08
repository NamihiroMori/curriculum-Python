from django.db import models

# goods_categoryテーブルのモデル
class Category(models.Model):
    name = models.CharField("カテゴリー名", max_length=32)

    class Meta:
        db_table = 'goods_category'
        verbose_name = verbose_name_plural = 'カテゴリー名'

# goods_productテーブルのモデル
class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField("商品名", max_length=128)
    price = models.PositiveIntegerField("価格")
    
    class Meta:
        db_table = 'goods_product'
        verbose_name = verbose_name_plural = '商品名'