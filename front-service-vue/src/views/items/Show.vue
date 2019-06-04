<template>
    <hr>
    <p>{{ item.title }}</p>
    <hr>
    <div class="row">
        <div class="col-md">
            <img :src="item.imageUrl" width="500" class="img-fluid">
        </div>
        <div class="col-md">
            <p>{{ item.title }}</p>
            <p>{{ item.description }}</p>
            <p>{{ item.price }} zł</p>
            <button href="" class="btn btn-lg btn-primary btn-block"
                    id="add-to-cart">Add to cart</button>
        </div>
    </div>
    <!-- Modal -->
    <div class="modal fade" id="myModal" role="dialog">
        <div class="modal-dialog">
            <!-- Modal content-->
            <div class="modal-content">
                <div class="modal-header">
                    <p> Notification </p>
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                </div>
                <div class="modal-body">

                    <img :src="item.imageUrl" width="200">
                    <p>{{ item.title }}</p>
                    <p>{{ item.price }} zł</p>
                    <p>Product has been added to cart</p>
                </div>
                <div class="modal-footer">
                    <button class="btn btn-lg btn-primary btn-bloc btn-close" data-dismiss="modal">Back to shop</button>
                    <a href="{{ path('buy_item_details') }}"><button class="btn btn-lg btn-primary btn-bloc">Go to check-in</button></a>
                </div>
            </div>
        </div>
    </div>
 </template>
<template v-else>
    <div>
        <p>No item to display, go back to home page</p>
    </div>
</template>

 <script>
 </script>

