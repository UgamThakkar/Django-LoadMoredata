let visible = 3;

const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')

$.ajax({
    type: "GET",
    url: `/posts-json/${visible}`,
    success: function(response) {
        // console.log(response.data)
        const data = response.data
        data.map(post =>{
            console.log(post.id)
        })
    },
    error: function(error) {
        console.log(error)
    }

})