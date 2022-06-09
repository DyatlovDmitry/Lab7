// $('.').click(function () {
//     var catid;
//     catid = $(this).attr("data-catid");
//     $.ajax(
//         {
//             type: "GET",
//             url: "/PageForPosts",
//             data: {
//                 post_id: catid
//             },
//             success: function (data) {
//                 $('#like' + catid).remove();
//                 $('#message').text(data);
//             }
//         })
// });
$(document).ready(function () {
    for (let MyButton of document.getElementsByTagName('button')) {
        if (MyButton.innerHTML === 'Like') {
            MyButton.innerHTML = 'Dislike'
            MyButton.style.background = 'red'
        } else {
            MyButton.innerHTML = 'Like'
            MyButton.style.background = 'blue'
        }
    }
    $('.form-for-like').submit(function () {
        const post_id = $(this).attr('id')
        console.log(String(post_id))
        $.ajax({
            type: $(this).attr('method'),
            url: 'http://127.0.0.1:8000/PageForPosts/',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'post_id': post_id,
            },
            // data: $(this).serialize(),
            success: function (response) {
                let MyButton = document.getElementById(`Button${post_id}`);
                console.log(MyButton.innerHTML)
                if (MyButton.innerHTML === 'Like') {
                    MyButton.innerHTML = 'Dislike'
                    MyButton.style.background = 'red'
                } else {
                    MyButton.innerHTML = 'Like'
                    MyButton.style.background = 'blue'
                }
                // $('.btn btn-danger').text("Like");
                // $('.quantity-of-likes').text(response["likes"]);
            },
            error: function (response) {
                console.log('error', response)
            }
        });
        return false;
    });
})