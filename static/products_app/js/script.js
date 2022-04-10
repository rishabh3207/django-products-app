async function getproducts() {
    const response = await fetch('/api/v1/product/');
    // Storing data in form of JSON
    var data = await response.json();
    showproducts(data);
}

async function getCategories() {
    const response = await fetch('/api/v1/category/');
    var data = await response.json();
    var categories_options = document.getElementById('category');
    categories_options.innerHTML = null;
    var newOption = document.createElement("option");
    newOption.value = "none";
    categories_options.options.add(newOption);
    for (let r of data) {
        var newOption = document.createElement("option");
        newOption.value = r.category_name;
        newOption.innerHTML = r.category_name;
        categories_options.options.add(newOption);
    }
}

getCategories();
getproducts();

async function getSubCategories(category, subCategory) {
    var category_name = document.getElementById(category);
    var subCategory_options = document.getElementById(subCategory);
    subCategory_options.innerHTML = null;
    const response = await fetch('/api/v1/category/search/?category=' + category_name.value);
    var data = await response.json();

    for (let r of data) {
        var newOption = document.createElement("option");
        newOption.value = r.subcategory_name;
        newOption.innerHTML = r.subcategory_name;
        subCategory_options.options.add(newOption);
    }
}

function showproducts(data) {
    let tab =
        `<thead>
        <tr>
            <th>&nbsp;&nbsp;</th>
            <th>Product</th>
            <th>Sub category</th>
            <th>Category</th>
        </tr>
        </thead>`;

    for (let r of data) {
        tab += `<tr> 
        <td><input class="checkbox" type="checkbox"></td>
        <td>${r.product_name} </td>
        <td>${r.subcategory.subcategory_name}</td> 
        <td>${r.subcategory.category.category_name}</td>         
        </tr>`;
    }

    document.getElementById("products").innerHTML = tab;
}

async function add_product() {
    var product_name = document.getElementById('product_name');
    var category_name = document.getElementById('category');
    var subcategory_name = document.getElementById('subCategory');
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "product-name": product_name.value,
        "sub-category": subcategory_name.value
    });
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw
    };

    const response = await fetch("/api/v1/product/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
    category_name.innerHTML = null;
    subcategory_name.innerHTML = null;
    getCategories();
    getproducts();
}