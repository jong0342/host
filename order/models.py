from django.db import models


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='주문시간')

    class Meta:
        db_table = 'jong_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'

"""
foreignkey(외래키)를 사용하여 user app 폴더내의 models.py 내외 User 클래스에서 외래키를 가져오겠다
on_delete=models.CASCADE는 만일 user,product 데이터값이 삭제될때 지금 Order의 설정한 models Order 클래스내의 있는 데이터 값도 같이 지우겠다는 설정
"""