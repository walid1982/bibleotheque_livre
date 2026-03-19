$(document).ready(function() {
    // Filtrage des livres par catégorie
    if (typeof categories !== 'undefined') {
        categories.forEach(function(category) {
            $('#category-' + category.id).click(function(e) {
                e.preventDefault();
                $('.book-item').hide();
                $('.category-' + category.id).show();
            });
        });
    } else {
        // Si le contexte Django n'est pas accessible, fallback sur les liens présents
        $('[id^=category-]').click(function(e) {
            e.preventDefault();
            var catId = $(this).attr('id').replace('category-', '');
            $('.book-item').hide();
            $('.category-' + catId).show();
        });
    }
});
