def apply_dis(price,dper):
    damt=price*dper/100
    print("Discount amt is ",damt)
    return price-damt
def add_gst(price,gstper):
    gstper=18
    gstamt=price*gstper/100
    print("GST amt is ",gstamt)
    return price+gstamt
def generate_invoice(cart,dper=0,gstper=18):
    stotal=0
    for prodname,price in cart.items():
        stotal+=price
    print("Subtotal before discount and gst is ",stotal)
    if(dper>0):
        dis_amt=apply_dis(stotal,dper)
    else:
        dis_amt=stotal
    final_tot=add_gst(dis_amt,gstper)
    print("Total amt after gst and discount is ",final_tot)
        
    