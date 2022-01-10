from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격') #숫자를 적을수있게 IntegerField 사용
    description = models.TextField(verbose_name='상품내용') #상품내용을 길게 적을수 있게 textField를 사용 제한이 없다
    stuck = models.IntegerField(verbose_name='재고')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.name

    
    class Meta:
        db_table = 'jong_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'


"""
일반적으로 상품의 정보를 표시할때는 상품명 상품가격 상품의 내용 그리고 재고수량과 상품이 등록된 날짜가 필요하다
상품명은 CharField로 표시 가능하고 가격은 숫자만 입력할것이기때문에 IntegerField로 생성한다.
상품의내용은 길게 적을수도있게 textfield로 설정해준 다음 재고도 숫자만입력할것이기 때문에 가격과 동일
상품의 등록날짜는 user.models.py에서 설정한 register_date와 동일하게 사용할것이다.
"""
