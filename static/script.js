/*
This code enables the page to refresh ultimatly enabling the tabulated vote to be updated thus giving the user the result of their vote right away
*/

function refreshPage() {
    window.location.reload();
} 

/*
This code enables the extra overflow text to be hidden until the user is able to click on it
 */

function alerta_upvote(vote) {
    vote = Number(vote) + 1
    alert('The current vote count is: ' + vote);
}

function alerta_downvote(vote) {
    vote = Number(vote) - 1;
    alert('The current vote count is: ' + vote);
}