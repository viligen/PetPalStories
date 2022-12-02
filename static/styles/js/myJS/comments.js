function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}

const renderCommentsList = (comments) => {

    const commentItems = comments.map(comment => `
            <div class="row border  rounded bg-light p-2 mb-1">
                <div class="col-sm-6"><strong class="border border-info rounded-circle bg-info bg-opacity-50 p-1">${comment.owner.username}</strong> : ${comment.text}</div>
                <div class="col-sm-6 ps-5 text-muted text-end">commented on: ${new Date(comment.published_on).toUTCString()}</div>
            </div>`);

    return `<div class="mt-2 ps-4">${commentItems.join(' ')}</div>`
};

function getPostComments(ev) {
    if (ev.target.tagName === 'BUTTON' && ev.target.textContent === 'See Comments') {
        let post_pk = ev.target.dataset.id

        fetch("/api/comments/?query=" + post_pk)
            .then(response => response.json())

            .then(comments => {


                let dataId = "comments-per-post" + post_pk

                document.querySelector(`div[data-name=${CSS.escape(dataId)}]`).innerHTML =
                    renderCommentsList(comments);

            });


    } else if (ev.target.tagName === 'BUTTON' && ev.target.type === 'submit') {
        ev.preventDefault()

        const post_id = ev.target.dataset.post
        const user_id = ev.target.dataset.user

        const csrf_token = document.cookie
            .split('; ')
            .find(row => row.startsWith('csrftoken'))
            .split('=')[1];


        const textElement = document.getElementById(`${post_id}`)
        const textValue = textElement.value

        const data = JSON.stringify({
                'text': textValue,
                'owner': {'id': user_id, 'username': 'username'},
                'parent_post': {'id': post_id},
            }
        )


        if (textValue.trim() !== '') {
            fetch("/api/comments/add/", {
                method: 'POST',
                headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrf_token},
                body: data
            })
                .then(response => response.json())
            textElement.value = ''

            delay(300).then(() => document.querySelector(`button[data-id=${CSS.escape(post_id)}]`).click());


        }
    }

}

window.onload = () => {
    document.querySelector('div[data-id="comments"]').addEventListener("click", getPostComments)
}