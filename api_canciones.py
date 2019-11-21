from add_order_songs import ord_libreria


## Implementamos la api que usaremos para sacar datos de la lista.
## Random = order  def get_order
## get_author !=     def get_author
## get_title        def get_title
''' 
<track>
     <name>Insert coin</name>
     <path>C:\USERS\YO\DESKTOP\CANCIONES\LAS_QUE_ME_DISGUSTAN</path>
</track>
'''
def get_order(ord_libreria):
    order = ord_libreria.get("order")
    return order

def get_author(ord_libreria):
    author = ord_libreria.get("artist")
    return author

def get_titles(ord_libreria):
    titles = ord_libreria.keys()
    return titles