<template>
    <div class="container">
        <h3 align="center" class="display-4"> Cart </h3>
        <table class="table">
            <thead>
                <tr>
                    <th> No. </th>
                    <th> Name </th>
                    <th> Category </th>
                    <th> Price </th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                    <tr v-for="(product, index) in products">
                        <td> {{ index }} </td>
                        <td> {{ product.name }} </td>
                        <td> {{ product.category.name }} </td>
                        <td> {{ product.price }} </td>
                        <td>
                            <b-button variant="danger" > Delete </b-button>
                        </td>
                    </tr>
            </tbody>
        </table>
        <div class="modal-footer">
            <b-button variant="info" to="/"> Back to shop </b-button>
            <b-button variant="success" to="/delivery"> Delivery </b-button>
        </div>
    </div>
</template>