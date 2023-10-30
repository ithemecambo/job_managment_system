
function logoutAction() {
    Swal.fire({
        "title": "Logout",
        "text": "Are you sure you want to logout from system?",
        "icon": "question",
        "showCancelButton": true,
        "cancelButtonText": "Cancel",
        "confirmButtonText": "Yes",
        "reverseButtons": true,
        "confirmButtonColor": "red"
    })
    .then(function(result) {
        if (result.isConfirmed) {
            console.log('You have been success log out of the system.')
        }
    })
}

function deleteAction(id, name, url) {
    console.log(name + ' => ' + url)
    Swal.fire({
        "title": "Delete",
        "text": "Are you sure you want to delete \"" + name + "\"?",
        "icon": "error",
        "showCancelButton": true,
        "cancelButtonText": "Cancel",
        "confirmButtonText": "Yes",
        "reverseButtons": true,
        "confirmButtonColor": "red"
    })
    .then(function(result) {
        if (result.isConfirmed) {
            window.location.href = url + '/' + id
            Swal.fire({
                'title': 'Success',
                'text': 'Todo  deleted success.',
                'icon': 'success',
                'showConfirmButton': false,
                'timer': 5000
            });
//            $.ajax({
//                url: url + '/' + id,
//                dataType: 'json'
//            })
//            .done(function(data) {
//                Swal.fire({
//                    'title': 'Success',
//                    'text': 'Todo  deleted success.',
//                    'icon': 'success',
//                    'showConfirmButton': false,
//                    'timer': 2000
//                });
//            })
//            .fail(function() {
//                Swal.fire("!Opps", "Something went wrong, try again later", "error");
//            })
        }
    })
}
