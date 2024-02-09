function toggleLike(publicationId) {
    $.ajax({
        type: 'POST',
        url: `/api/publications/${publicationId}/like/`,
        success: function(data) {
            console.log('Like added successfully');
        },
        error: function(error) {
            console.log('Error adding like');
        }
    });
}

function toggleUnlike(publicationId) {
    $.ajax({
        type: 'DELETE',
        url: `/api/publications/${publicationId}/like/`,
        success: function(data) {
            console.log('Like removed successfully');
        },
        error: function(error) {
            console.log('Error removing like');
        }
    });
}
