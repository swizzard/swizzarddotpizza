$(document).ready(function(){
    $("#one").on('click', function() {$(this).load("{% url 'hash_to_hash.views.consent' %}")});
    $("#two").on('click', function() { $(this).load('static/test2.html')});
    $("#three").on('click', function() { $(this).load('static/test3.html')});
});
