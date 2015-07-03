$(document).ready(function() {
    window.categories = [];
});

$(document).on("click", "#addCategory", function() {
    
    var questions;
    $.ajax({
      type: 'GET',
      url: "/getQuestions/",
      data: {
        category: $("#categorySelect").val(),
      },
      success: function(data) {
        questions = eval(data);
      },
      async:false
    });
    
    var questionObject = {};
    for (var i = 1; i <= 5; ++i) {
        questionObject[100 * i] = [];
    }
    for (var i = 0; i < questions.length; ++i) {
        var price = questions[i].fields.price;
        questionObject[price].push([questions[i].fields.statement, questions[i].pk]);
    }
    
    var response = $("<div>").addClass('newCategory').attr('id', window.categories.length.toString());
    
    response.append($("<h4>").text($("#categorySelect :selected").text()).addClass("text-center"));

    window.categories.push($("#categorySelect").val());

    for (var i = 1; i <= 5; ++i) {
        var currentPrice = $("<div>").addClass("form-group");
        currentPrice.append($("<label>").text(100 * i).addClass("col-sm-1").addClass("control-label"));

        var select = $("<select>").attr("name", 100 * i).addClass("form-control");

        for (var j = 0; j < questionObject[100 * i].length; ++j) {
            select.append($("<option>").attr("value", questionObject[100 * i][j][1]).text(questionObject[100 * i][j][0]));
        }
        currentPrice.append($("<div>").addClass("col-sm-11").append(select));
        response.append(currentPrice);
    }
    $("#categories").append(response);
});

$(document).on("click", "#magic", function() {
    var gameId;
    $.ajax({
        type: 'POST',
        url: "/registerGame/",
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function(data) {
            console.log(data);
            gameId = data;
        },
        async:false
    });

    console.log(gameId);
    for (var i = 0; i < categories.length; ++i) {
        var result = {"category" : categories[i]};
        result["game"] = gameId;
        $("#" + i.toString()).children().each(function() {
            if ($(this).prop("tagName") == "SELECT") {
                //console.log($(this).attr("name"), $("option:selected", this).val());

                result[parseInt($(this).attr("name"))] = $("option:selected", this).val();
            }
        });
        $.ajax({
            type: 'POST',
            url: "/addCategoryToGame/",
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            data : result,
            success: function(data) {
                console.log(data);
                gameId = data;
            },
            async: true
        });
    }
    alert("Success");
    window.location.replace("/game/" + gameId.toString());
});