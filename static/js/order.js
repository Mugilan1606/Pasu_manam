
function updateQuantity(){

let product=document.getElementById("product").value

let quantity=document.getElementById("quantity")

quantity.innerHTML=""

let options=[]


if(product=="milk"){

options=[
"250ml-15",
"500ml-30",
"1litre-60"
]

}

if(product=="curd"){

options=[
"250ml-25",
"500ml-50",
"1litre-100"
]

}

if(product=="ghee"){

options=[
"100g-50",
"250g-150",
"500g-250",
"1litre-500"
]

}


options.forEach(function(item){

let parts=item.split("-")

let option=document.createElement("option")

option.value=parts[1]

option.text=item.replace("-", " - ₹")

quantity.appendChild(option)

})

}



function calculateTotal(){

let price=document.getElementById("quantity").value

document.getElementById("total").value="₹ "+price

}
