<template>
    <div class="container">
        <a href="{{}}" class="btn btn-primary pull-right">
            Create <span class="fa fa-plus-circle"></span>
        </a>
        <h1>All Products</h1>

        <table class="table">
            <thead>
                <tr>
                    <th>Title</th>
                    <th class="d-none d-md-table-cell">Description</th>
                    <th>Category</th>
                    <th>Price</th>
                    <th>&nbsp;</th>
                    <th>&nbsp;</th>
                </tr>
            </thead>
            <tbody>
                    <tr v-for="product in products">
                        <td>{{ product.title }}</td>
                        <td class="d-none d-md-table-cell">{{ product.description }}</td>
                        <td>{{ product.category }}</td>
                        <td>{{ product.price }}</td>
                        <td>
                            <a href="">
                               <i class="far fa-edit"></i>
                            </a>
                        </td>
                        <td>
                            <a href="" class="delete">
                               <i class="fa fa-trash"></i>
                            </a>
                        </td>
                    </tr>
            </tbody>
        </table>
    </div>
</template>

