from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, static_url_path='/static')

Productnum = ""
Stock = 0
PaintStock = 5
YarnStock = 11
CanvasStock = 2
GelPensStock = 8
SewNeedleStock = 15
MarkersStock = 5
ToteStock = 100
PaperStock = 25
ResinStock = 7
GlueStock = 18
CartArray = []
CartPrice = []
qtyarry = []
OrderNum = 10001
InvoiceNum = 10001
Total = 0

ClickPaint = 1
ClickYarn = 1
ClickCanvas = 1
ClickGelPens = 1
ClickSewNeedles = 1
ClickMarkers = 1
ClickMarkers = 1
ClickTote = 1
ClickPaper = 1
ClickResin = 1
ClickGlue = 1


YarnUserQty = 0
GelPensUserQty = 0
CanvasUserQty = 0
GlueUserQty = 0
MarkersUserQty = 0
PaintUserQty = 0
ResinUserQty = 0
SewNeedlesUserQty = 0
ToteUserQty = 0
PaperUserQty = 0


Name = ""
shipping = ""
billing = ""
card = ""


users = {}

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('SunnyLife_Login.html')
    else:
        username = request.form.get("txtUser")
        password = request.form.get("txtPass")
        
        if not username or not password:
            return render_template('SunnyLife_Login.html', msg1="Please enter both username and password.")
        
        return check_login(username, password)

def check_login(username, password):
    if username in users and users[username]['password'] == password:
        return redirect(url_for('home', username=username))
    else:
        return render_template('SunnyLife_Login.html', msg1="Invalid username or password.")

@app.route('/home')
def home():
    username = request.args.get('username')
    if username:
        return render_template('home.html', username=username)
    else:
        return redirect(url_for('main'))

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'GET':
        return render_template('SunnyLife_Signup.html')
    elif request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        shipping_address = request.form.get('address')
        billing_address = request.form.get('Billing-Address')
        card_info = request.form.get('Card-Info')
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users:
            return render_template('SunnyLife_Signup.html', msg="Username already exists.")
        else:
            users[username] = {
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
                'shipping_address': shipping_address,
                'billing_address': billing_address,
                'card_info': card_info
            }
            return redirect(url_for('main'))

@app.route('/edit_info', methods=['POST'])
def edit_info():
    username = request.args.get('username')
    if not username:
        return redirect(url_for('main'))

    if request.method == 'POST':
        name = request.form.get('txtEditName')
        shipping = request.form.get('txtEditShipping')
        billing = request.form.get('txtEditBilling')
        card = request.form.get('txtEditCard')
        
        if username in user_info:
            if name:
                user_info[username]['Name'] = name
            if shipping:
                user_info[username]['Shipping'] = shipping
            if billing:
                user_info[username]['Billing'] = billing
            if card:
                user_info[username]['Card'] = card
                
        return redirect(url_for('home', username=username))



def ProductAmount(Productnum):
    global Stock, PaintStock, YarnStock, CanvasStock, GelPensStock, SewNeedleStock, MarkersStock, ToteStock, PaperStock, ResinStock, GlueStock
    
    match Productnum:
        case 111:
            Stock = PaintStock
        case 123:
            Stock = YarnStock
        case 134:
            Stock = CanvasStock
        case 176:
            Stock = GelPensStock
        case 145:
            Stock = SewNeedleStock
        case 486:
            Stock = MarkersStock
        case 190:
            Stock = ToteStock
        case 129:
            Stock = PaperStock
        case 284:
            Stock = ResinStock
        case 155:
            Stock = GlueStock
        case _:
            Stock = 0
    return Stock

@app.route('/PaintProduct', methods=['GET', 'POST'])
def PaintProduct():
    if request.method == 'GET':
        Productnum = 111
        Price = 20.99
        Stock = ProductAmount(Productnum)
        msg = ""
        if Stock == 0:
            msg = "Out of stock"
        elif Stock < 10:
            msg = "Low stock"
        else:
            msg = "In stock"
        return render_template('PaintProduct.html', msg=msg)
    else:
        Action = PaintAction()
        return Action

def PaintAction():
    global ClickPaint,PaintUserQty,PaintFullPrice
    if ClickPaint == 1:
        UserQty = request.form.get("cmbPaintQty")
        FullPrice = int(UserQty) * 20.99
        PaintUserQty = UserQty
        PaintFullPrice = FullPrice
        CartArray.append("111")
        CartPrice.append(FullPrice)
        qtyarry.append(UserQty)
        Total = sum(CartPrice)
        ClickPaint =+ 1 
        return render_template('Cart.html',PaintUserQty=PaintUserQty, Total=Total)
    else:
        CartArray.remove("111")
        CartPrice.remove(PaintUserQty)
        qtyarry.remove(PaintFullPrice)
        
        UserQty = request.form.get("cmbPaintQty")
        FullPrice = int(UserQty) * 20.99
        PaintUserQty += UserQty
        PaintFullPrice += FullPrice

        CartArray.append("111")
        CartPrice.append(PaintUserQty)
        qtyarry.append(PaintFullPrice)
        Total = sum(CartPrice)
        ClickPaint =+ 1
        return render_template('Cart.html',PaintUserQty=PaintUserQty, Total=Total)
        

@app.route('/YarnProduct', methods=['GET', 'POST'])
def YarnProduct():
    if request.method == 'GET':
        Productnum = 123
        Price = 8.99
        Stock = ProductAmount(Productnum)
        msg = ""
        if Stock == 0:
            msg = "Out of stock"
        elif Stock < 10:
            msg = "Low stock"
        else:
            msg = "In stock"
        return render_template('YarnProduct.html', msg=msg)
    else:
        YAction = YarnAction()
        return YAction

def YarnAction():
    global ClickYarn,YarnUserQty,YarnFullPrice
    if ClickYarn == 1:
        UserQty = request.form.get("cmbYarnQty")
        FullPrice = int(UserQty) * 8.99
        YarnUserQty = UserQty
        YarnFullPrice = FullPrice
        CartArray.append("123")
        CartPrice.append(FullPrice)
        qtyarry.append(UserQty)
        Total = sum(CartPrice)
        ClickYarn =+ 1 
        return render_template('Cart.html', YarnUserQty=YarnUserQty, Total=Total)
    else:
        CartArray.remove("123")
        CartPrice.remove(YarnUserQty)
        qtyarry.remove(YarnFullPrice)
        
        UserQty = request.form.get("cmbYarnQty")
        FullPrice = int(UserQty) * 8.99
        YarnUserQty += UserQty
        YarnFullPrice += FullPrice

        CartArray.append("123")
        CartPrice.append(YarnUserQty)
        qtyarry.append(YarnUserQty)
        Total = sum(CartPrice)
        ClickPaint =+ 1
        return render_template('Cart.html',YarnUserQty=YarnUserQty, Total=Total)

@app.route('/CanvasProduct', methods=['GET', 'POST'])
def CanvasProduct():
    if request.method == 'GET':
        Productnum = 134
        Price = 16.99
        Stock = ProductAmount(Productnum)
        msg = ""
        if Stock == 0:
            msg = "Out of stock"
        elif Stock < 10:
            msg = "Low stock"
        else:
            msg = "In stock"
        return render_template('CanvasProduct.html', msg=msg)
    else:
        CAction = CanvasAction()
        return CAction

def CanvasAction():
    global ClickCanvas,CanvasUserQty,CanvasFullPrice
    if ClickCanvas == 1:
        UserQty = request.form.get("cmbCanvaQty")
        FullPrice = int(UserQty) * 16.99
        CanvasUserQty = UserQty
        CanvasFullPrice = FullPrice
        CartArray.append("134")
        CartPrice.append(FullPrice)
        qtyarry.append(UserQty)
        Total = sum(CartPrice)
        ClickCanvas =+ 1 
        return render_template('Cart.html', CanvasUserQty=CanvasUserQty, Total=Total)
    else:
        CartArray.remove("134")
        CartPrice.remove(CanvasUserQty)
        qtyarry.remove(CanvasFullPrice)
        
        UserQty = request.form.get("cmbCanvaQty")
        FullPrice = int(UserQty) * 16.99
        CanvasUserQty += UserQty
        CanvasFullPrice += FullPrice

        CartArray.append("134")
        CartPrice.append(CanvasUserQty)
        qtyarry.append(CanvasUserQty)
        Total = sum(CartPrice)
        ClickPaint =+ 1
        return render_template('Cart.html',YarnUserQty=YarnUserQty, Total=Total)
    
@app.route('/GelPensProduct', methods=['GET', 'POST'])
def GelPensProduct():
    global Productnum, Price
    if request.method == 'GET':
        Productnum = 176
        Price = 10.59
        Stock = ProductAmount(Productnum)
        msg = ""
        if Stock == 0:
            msg = "Out of stock"
        elif Stock < 10:
            msg = "Low stock"
        else:
            msg = "In stock"
        return render_template('GelPensProduct.html', msg=msg)
    else:
        GPAction = GelPensAction()
        return GPAction

def GelPensAction():
    global ClickGelPens,GelPensUserQty,GelPensFullPrice
    if ClickGelPens == 1:
        UserQty = request.form.get("cmbGelPensQty")
        FullPrice = int(UserQty) * 10.59
        GelPensUserQty = UserQty
        GelPensFullPrice = FullPrice
        CartArray.append("176")
        CartPrice.append(FullPrice)
        qtyarry.append(UserQty)
        Total = sum(CartPrice)
        ClickGelPens =+ 1 
        return render_template('Cart.html', GelPensUserQty=GelPensUserQty, Total=Total)
    else:
        CartArray.remove("176")
        CartPrice.remove(GelPensUserQty)
        qtyarry.remove(GelPensFullPrice)
        
        UserQty = request.form.get("cmbGelPensQty")
        FullPrice = int(UserQty) * 10.59
        GelPensUserQty += UserQty
        GelPensFullPrice += FullPrice

        CartArray.append("176")
        CartPrice.append(GelPensUserQty)
        qtyarry.append(GelPensFullPrice)
        Total = sum(CartPrice)
        ClickGelPens =+ 1
        return render_template('Cart.html',GelPensUserQty=GelPensUserQty, Total=Total)

@app.route('/SewNeedleProduct', methods=['GET', 'POST'])
def SewNeedleProduct():
    if request.method == 'GET':
        Productnum = 145
        Price = 6.79
        Stock = ProductAmount(Productnum)
        msg = ""
        if Stock == 0:
            msg = "Out of stock"
        elif Stock < 10:
            msg = "Low stock"
        else:
            msg = "In stock"
        return render_template('SewNeedleProduct.html', msg=msg)
    else:
        SNAction = SewNeedlesAction()
        return SNAction

def SewNeedlesAction():
    global ClickSewNeedles, SewNeedlesUserQty, SewNeedlesFullPrice
    if ClickSewNeedles == 1:
        UserQty = request.form.get("cmbSewNeedleQty")
        FullPrice = int(UserQty) * 6.79
        SewNeedlesUserQty = UserQty
        SewNeedlesFullPrice = FullPrice
        CartArray.append("145")
        CartPrice.append(FullPrice)
        qtyarry.append(UserQty)
        Total = sum(CartPrice)
        ClickSewNeedles += 1
        return render_template('Cart.html', SewNeedlesUserQty=SewNeedlesUserQty, Total=Total)
    else:
        CartArray.remove("145")
        CartPrice.remove(SewNeedlesFullPrice)
        qtyarry.remove(SewNeedlesUserQty)

        UserQty = request.form.get("cmbSewNeedleQty")
        FullPrice = int(UserQty) * 6.79
        SewNeedlesUserQty += int(UserQty)
        SewNeedlesFullPrice += FullPrice

        CartArray.append("145")
        CartPrice.append(SewNeedlesFullPrice)
        qtyarry.append(SewNeedlesUserQty)
        Total = sum(CartPrice)
        ClickSewNeedles += 1
        return render_template('Cart.html', SewNeedlesUserQty=SewNeedlesUserQty, Total=Total)

@app.route('/MarkersProduct', methods=['GET', 'POST'])
def MarkersProduct():
    if request.method == 'GET':
        Productnum = 486
        Price = 29.99
        Stock = ProductAmount(Productnum)
        msg = ""
        if Stock == 0:
            msg = "Out of stock"
        elif Stock < 10:
            msg = "Low stock"
        else:
            msg = "In stock"
        return render_template('MarkersProduct.html', msg=msg)
    else:
        MAction = MarkersAction()
        return MAction

def MarkersAction():
    global ClickMarkers, MarkersUserQty, MarkersFullPrice
    if ClickMarkers == 1:
        UserQty = request.form.get("cmbMarkersQty")
        FullPrice = int(UserQty) * 29.99
        MarkersUserQty = int(UserQty)
        MarkersFullPrice = FullPrice
        CartArray.append("486")
        CartPrice.append(FullPrice)
        qtyarry.append(UserQty)
        Total = sum(CartPrice)
        ClickMarkers += 1
        return render_template('Cart.html', MarkersUserQty=MarkersUserQty, Total=Total)
    else:
        CartArray.remove("486")
        CartPrice.remove(MarkersFullPrice)
        qtyarry.remove(MarkersUserQty)

        UserQty = request.form.get("cmbMarkersQty")
        FullPrice = int(UserQty) * 29.99
        MarkersUserQty += int(UserQty)
        MarkersFullPrice += FullPrice

        CartArray.append("486")
        CartPrice.append(MarkersFullPrice)
        qtyarry.append(MarkersUserQty)
        Total = sum(CartPrice)
        ClickMarkers += 1
        return render_template('Cart.html', MarkersUserQty=MarkersUserQty, Total=Total)

@app.route('/ToteProduct', methods=['GET', 'POST'])
def ToteProduct():
    if request.method == 'GET':
        Productnum = 190
        Price = 5.50
        Stock = ProductAmount(Productnum)
        msg = ""
        if Stock == 0:
            msg = "Out of stock"
        elif Stock < 10:
            msg = "Low stock"
        else:
            msg = "In stock"
        return render_template('ToteProduct.html', msg=msg)
    else:
        TAction = ToteAction()
        return TAction

def ToteAction():
    global ClickTote, ToteUserQty, ToteFullPrice
    if ClickTote == 1:
        UserQty = request.form.get("cmbToteQty")
        FullPrice = int(UserQty) * 5.50
        ToteUserQty = int(UserQty)
        ToteFullPrice = FullPrice
        CartArray.append("190")
        CartPrice.append(FullPrice)
        qtyarry.append(UserQty)
        Total = sum(CartPrice)
        ClickTote += 1
        return render_template('Cart.html', ToteUserQty=ToteUserQty, Total=Total)
    else:
        CartArray.remove("190")
        CartPrice.remove(ToteFullPrice)
        qtyarry.remove(ToteUserQty)

        UserQty = request.form.get("cmbToteQty")
        FullPrice = int(UserQty) * 5.50
        ToteUserQty += int(UserQty)
        ToteFullPrice += FullPrice

        CartArray.append("190")
        CartPrice.append(ToteFullPrice)
        qtyarry.append(ToteUserQty)
        Total = sum(CartPrice)
        ClickTote += 1
        return render_template('Cart.html', ToteUserQty=ToteUserQty, Total=Total)

@app.route('/PaperProduct', methods=['GET', 'POST'])
def PaperProduct():
    if request.method == 'GET':
        Productnum = 129
        Price = 15.50
        Stock = ProductAmount(Productnum)
        msg = ""
        if Stock == 0:
            msg = "Out of stock"
        elif Stock < 10:
            msg = "Low stock"
        else:
            msg = "In stock"
        return render_template('PaperProduct.html', msg=msg)
    else:
        PapAction = PaperAction()
        return PapAction

def PaperAction():
    global ClickPaper, PaperUserQty, PaperFullPrice
    if ClickPaper == 1:
        UserQty = request.form.get("cmbPaperQty")
        FullPrice = int(UserQty) * 15.50
        PaperUserQty = int(UserQty)
        PaperFullPrice = FullPrice
        CartArray.append("129")
        CartPrice.append(FullPrice)
        qtyarry.append(UserQty)
        Total = sum(CartPrice)
        ClickPaper += 1
        return render_template('Cart.html', PaperUserQty=PaperUserQty, Total=Total)
    else:
        CartArray.remove("129")
        CartPrice.remove(PaperFullPrice)
        qtyarry.remove(PaperUserQty)

        UserQty = request.form.get("cmbPaperQty")
        FullPrice = int(UserQty) * 15.50
        PaperUserQty += int(UserQty)
        PaperFullPrice += FullPrice

        CartArray.append("129")
        CartPrice.append(PaperFullPrice)
        qtyarry.append(PaperUserQty)
        Total = sum(CartPrice)
        ClickPaper += 1
        return render_template('Cart.html', PaperUserQty=PaperUserQty, Total=Total)

@app.route('/ResinProduct', methods=['GET', 'POST'])
def ResinProduct():
    if request.method == 'GET':
        Productnum = 284
        Price = 40.90
        Stock = ProductAmount(Productnum)
        msg = ""
        if Stock == 0:
            msg = "Out of stock"
        elif Stock < 10:
            msg = "Low stock"
        else:
            msg = "In stock"
        return render_template('ResinProduct.html', msg=msg)
    else:
        RAction = ResinAction()
        return RAction

def ResinAction():
    global ClickResin, ResinUserQty, ResinFullPrice
    if ClickResin == 1:
        UserQty = request.form.get("cmbResinQty")
        FullPrice = int(UserQty) * 40.90
        ResinUserQty = int(UserQty)
        ResinFullPrice = FullPrice
        CartArray.append("284")
        CartPrice.append(FullPrice)
        qtyarry.append(UserQty)
        Total = sum(CartPrice)
        ClickResin += 1
        return render_template('Cart.html', ResinUserQty=ResinUserQty, Total=Total)
    else:
        CartArray.remove("284")
        CartPrice.remove(ResinFullPrice)
        qtyarry.remove(ResinUserQty)

        UserQty = request.form.get("cmbResinQty")
        FullPrice = int(UserQty) * 40.90
        ResinUserQty += int(UserQty)
        ResinFullPrice += FullPrice

        CartArray.append("284")
        CartPrice.append(ResinFullPrice)
        qtyarry.append(ResinUserQty)
        Total = sum(CartPrice)
        ClickResin += 1
        return render_template('Cart.html', ResinUserQty=ResinUserQty, Total=Total)

@app.route('/GlueProduct', methods=['GET', 'POST'])
def GlueProduct():
    if request.method == 'GET':
        Productnum = 155
        Price = 17.35
        Stock = ProductAmount(Productnum)
        msg = ""
        if Stock == 0:
            msg = "Out of stock"
        elif Stock < 10:
            msg = "Low stock"
        else:
            msg = "In stock"
        return render_template('GlueProduct.html', msg=msg)
    else:
        GAction = GlueAction()
        return GAction

def GlueAction():
    global ClickGlue, GlueUserQty, GlueFullPrice
    if ClickGlue == 1:
        UserQty = request.form.get("cmbGlueQty")
        FullPrice = int(UserQty) * 17.35
        GlueUserQty = int(UserQty)
        GlueFullPrice = FullPrice
        CartArray.append("155")
        CartPrice.append(FullPrice)
        qtyarry.append(UserQty)
        Total = sum(CartPrice)
        ClickGlue += 1
        return render_template('Cart.html', GlueUserQty=GlueUserQty,Total=Total)
    else:
        CartArray.remove("155")
        CartPrice.remove(GlueFullPrice)
        qtyarry.remove(GlueUserQty)

        UserQty = request.form.get("cmbGlueQty")
        FullPrice = int(UserQty) * 17.35
        GlueUserQty += int(UserQty)
        GlueFullPrice += FullPrice

        CartArray.append("155")
        CartPrice.append(GlueFullPrice)
        qtyarry.append(GlueUserQty)
        Total = sum(CartPrice)
        ClickGlue += 1
        return render_template('Cart.html', GlueUserQty=GlueUserQty,Total=Total)


@app.route('/RemovePaint')
def RemovePaint():
    CartArray.remove("111")
    CartPrice.remove(PaintFullPrice)
    qtyarry.remove(PaintUserQty)
    return render_template('Cart.html')

@app.route('/RemoveYarn')
def RemoveYarn():
    CartArray.remove("123")
    CartPrice.remove(YarnFullPrice)
    qtyarry.remove(YarnUserQty)
    return render_template('Cart.html')
@app.route('/RemoveCanvas')
def RemoveCanvas():
    CartArray.remove("134")
    CartPrice.remove(CanvasFullPrice)
    qtyarry.remove(CanvasUserQty)
    return render_template('Cart.html')
@app.route('/RemoveGelPens')
def RemoveGelPens():
    CartArray.remove("176")
    CartPrice.remove(GelPensFullPrice)
    qtyarry.remove(GelPensUserQty)
    return render_template('Cart.html')
@app.route('/RemoveSewNeedles')
def RemoveSewNeedles():
    CartArray.remove("145")
    CartPrice.remove(SewNeedlesFullPrice)
    qtyarry.remove(SewNeedlesUserQty)
    return render_template('Cart.html')
@app.route('/RemoveMarkers')
def RemoveMarkers():
    CartArray.remove("486")
    CartPrice.remove(MarkersFullPrice)
    qtyarry.remove(MarkersUserQty)
    return render_template('Cart.html')
@app.route('/RemoveTote')
def RemoveTote():
    CartArray.remove("190")
    CartPrice.remove(ToteFullPrice)
    qtyarry.remove(ToteUserQty)
    return render_template('Cart.html')
@app.route('/RemovePaper')
def RemovePaper():
    CartArray.remove("129")
    CartPrice.remove(PaperFullPrice)
    qtyarry.remove(PaperUserQty)
    return render_template('Cart.html')
@app.route('/RemoveResin')
def RemoveResin():
    CartArray.remove("284")
    CartPrice.remove(ResinFullPrice)
    qtyarry.remove(ResinUserQty)
    return render_template('Cart.html')
@app.route('/RemoveGlue')
def RemoveGlue():
    CartArray.remove("155")
    CartPrice.remove(GlueFullPrice)
    qtyarry.remove(GlueUserQty)
    return render_template('Cart.html')


@app.route('/Admin', methods=['GET', 'POST'])
def Admin():
    global Stock, PaintStock, YarnStock, CanvasStock, GelPensStock, SewNeedleStock, MarkersStock, ToteStock, PaperStock, ResinStock, GlueStock
    if (request.method == 'GET'):
        return render_template("Admin.html",PaintStock=PaintStock, YarnStock=YarnStock, CanvasStock=CanvasStock,
                               GelPensStock=GelPensStock, SewNeedleStock=SewNeedleStock, MarkersStock=MarkersStock,
                               ToteStock=ToteStock, PaperStock=PaperStock, ResinStock=ResinStock, GlueStock=GlueStock)
    elif (request.method == 'POST'):
        Act = PlusMinus()
        return Act





@app.route('/update_stock', methods=['POST'])
def update_stock():
    PaintStock = int(request.form.get("txtEditPaint", 0))
    YarnStock = int(request.form.get("txtEditYarn", 0))
    CanvasStock = int(request.form.get("txtEditCanvas", 0))
    GelPensStock = int(request.form.get("txtEditGelPens", 0))
    SewNeedleStock = int(request.form.get("txtEditSewNeedles", 0))
    MarkersStock = int(request.form.get("txtEditMarkers", 0))
    ToteStock = int(request.form.get("txtEditTote", 0))
    PaperStock = int(request.form.get("txtEditPaper", 0))
    ResinStock = int(request.form.get("txtEditResin", 0))
    GlueStock = int(request.form.get("txtEditGlue", 0))
    
    return render_template("Admin.html", 
                           PaintStock=PaintStock, 
                           YarnStock=YarnStock, 
                           CanvasStock=CanvasStock,
                           GelPensStock=GelPensStock, 
                           SewNeedleStock=SewNeedleStock, 
                           MarkersStock=MarkersStock,
                           ToteStock=ToteStock, 
                           PaperStock=PaperStock, 
                           ResinStock=ResinStock, 
                           GlueStock=GlueStock)




    
def PlusMinus():
    global Stock, PaintStock, YarnStock, CanvasStock, GelPensStock, SewNeedleStock, MarkersStock, ToteStock, PaperStock, ResinStock, GlueStock
    
    Product = request.form.get("txtWhich")
    Product = int(Product)
    Operation = request.form.get("cmbOperation")
    Operation = str(Operation)
    ProductQty = request.form.get("txtHowMuch")
    ProductQty = int(ProductQty)
    
    if Operation == "+":
        match Product:
            case "111":
                PaintStock += ProductQty
            case "123":
                YarnStock += ProductQty
            case "134":
                CanvasStock += ProductQty
            case "176":
                GelPensStock += ProductQty
            case "145":
                SewNeedleStock += ProductQty
            case "486":
                MarkersStock += ProductQty
            case "190":
                ToteStock += ProductQty
            case "129":
                PaperStock += ProductQty
            case "284":
                ResinStock += ProductQty
            case "155":
                GlueStock += ProductQty
            case _:
                print("0")
                
    elif Operation == '-':
        match Product:
            case 111:
                PaintStock -= ProductQty 
            case 123:
                YarnStock -= ProductQty 
            case 134:
                CanvasStock -= ProductQty 
            case 176:
                GelPensStock -= ProductQty
            case 145:
                SewNeedleStock -= ProductQty 
            case 486:
                MarkersStock -= ProductQty 
            case 190:
                ToteStock -= ProductQty 
            case 129:
                PaperStock -= ProductQty
            case 284:
                ResinStock -= ProductQty
            case 155:
                GlueStock -= ProductQty
            case _:
                print("0")
                
    return render_template("Admin.html",PaintStock=PaintStock, YarnStock=YarnStock, CanvasStock=CanvasStock, 
                            GelPensStock=GelPensStock, SewNeedleStock=SewNeedleStock, 
                            MarkersStock=MarkersStock, ToteStock=ToteStock, PaperStock=PaperStock, 
                            ResinStock=ResinStock, GlueStock=GlueStock)
                

@app.route('/Cart', methods=['GET', 'POST'])
def Cart():
    if request.method == 'GET':
        return render_template('Cart.html', YarnUserQty=YarnUserQty, GelPensUserQty=GelPensUserQty, Total=Total, CanvasUserQty=CanvasUserQty, GlueUserQty=GlueUserQty, MarkersUserQty=MarkersUserQty, PaintUserQty=PaintUserQty, ResinUserQty=ResinUserQty, SewNeedlesUserQty=SewNeedlesUserQty, ToteUserQty=ToteUserQty, PaperUserQty=PaperUserQty)

@app.route('/ShowInfo')
def ShowInfo():
    # Assuming you have obtained the username from the session or request parameters
    username = request.args.get('username')
    if username in users:
        user_info = users[username]
        return render_template("ShowInfo.html", Name=user_info.get('first_name', ''), Shipping=user_info.get('shipping_address', ''), Billing=user_info.get('billing_address', ''), Card=user_info.get('card_info', ''))
    
    # If the user is not found, still render the template without passing any user information
    return render_template("ShowInfo.html", Name='', Shipping='', Billing='', Card='')



@app.route('/Edit')
def Edit():
    # Assuming you have obtained the username from the session or request parameters
    username = request.args.get('username')
    if username in users:
        user_info = users[username]
        return render_template("Editinfo.html", Name=user_info.get('first_name', ''), shipping=user_info.get('shipping_address', ''), billing=user_info.get('billing_address', ''), card=user_info.get('card_info', ''))
    
    # If the user is not found, still render the template without passing any user information
    return render_template("Editinfo.html", Name='', shipping='', billing='', card='')

@app.route('/EditName', methods=['POST'])
def EditName():
    global Name
    if request.method == 'POST':
        Name = request.form.get("txtEditName")
        shipping = request.form.get("txtEditShipping")
        billing = request.form.get("txtEditBilling")
        card = request.form.get("txtEditCard")

        return render_template("Editinfo.html", Name=Name, Shipping=shipping, Billing=billing, Card=card)

@app.route('/EditShipping', methods=['POST'])
def EditShipping():
    global Shipping
    if request.method == 'POST':
        Shipping = request.form.get("txtEditShipping")
        return render_template("Editinfo.html", Name=Name,Shipping=shipping,Billing=billing,Card=card)

@app.route('/EditBilling', methods=['POST'])
def EditBilling():
    global Billing
    if request.method == 'POST':
        Billing = request.form.get("txtEditBilling")
        return render_template("Editinfo.html", Name=Name,Shipping=shipping,Billing=billing,Card=card)

@app.route('/EditCard', methods=['POST'])
def EditCard():
    global Card
    if request.method == 'POST':
        Card = request.form.get("txtEditCard")
        return render_template("Editinfo.html", Name=Name,Shipping=shipping,Billing=billing,Card=card)

@app.route('/GiveInvoice')
def GiveInvoice(): #fix Submit after edit info, cart 
    from datetime import date
    global CartArray, CartPrice, qtyarry, OrderNum, InvoiceNum,shipping,billing,Name,PaintStock, YarnStock, CanvasStock, GelPensStock, SewNeedleStock, MarkersStock,ToteStock, PaperStock, ResinStock, GlueStock
    
    OrderNum += 1  
    InvoiceNum += 1
    Total = sum(CartPrice)
    Tax = Total * 0.08875
    TaxTotal = Tax + Total
    todaydate = date.today()
    length = len(CartArray)
    
    Total = round(Total, 2)
    Tax = round(Tax, 2)
    TaxTotal = round(TaxTotal, 2)
    
    for qtyindex, product in enumerate(CartArray):
        qty = int(qtyarry[qtyindex]) 
    
        match product:
            case "111":
                PaintStock -= qty
            case "123":
                YarnStock -= qty
            case "134":
                CanvasStock -= qty
            case "176":
                GelPensStock -= qty
            case "145":
                SewNeedleStock -= qty
            case "486":
                MarkersStock -= qty
            case "190":
                ToteStock -= qty
            case "129":
                PaperStock -= qty
            case "284":
                ResinStock -= qty
            case "155":
                GlueStock -= qty
                
    return render_template("Invoice.html", Total=Total, Tax=Tax,
                           TaxTotal=TaxTotal, todaydate=todaydate,
                           OrderNum=OrderNum, InvoiceNum=InvoiceNum,
                           Name=Name, Shipping=shipping, Billing=billing,
                           CartArray=CartArray, qtyarry=qtyarry,
                           CartPrice=CartPrice,  length=length)
            
if __name__ == "__main__":
    app.run()
