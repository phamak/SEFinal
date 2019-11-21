$("form").on('submit', function (e) {
    $("").replaceAll(".hereugo")
    var inputs = $('#directionForm :input');
    var lat = inputs[0].value;
    var long = inputs[1].value;
    getDirections(lat, long);
    e.preventDefault();
});

function getDirections(lat, long) {
    var ghRouting = new GraphHopper.Routing({
        key: "26942361-2cf9-46ec-84e8-992443d9c724",
        vehicle: "car",
        elevation: false
    });

    ghRouting.addPoint(new GHInput(35.654579, -97.469490));
    ghRouting.addPoint(new GHInput(lat, long));

    ghRouting.doRequest()
    .then(function(json) {
        // Add your own result handling here
        success(json);
    })
    .catch(function(err) {
        console.error(err.message);
    });
};

function success(json) {
    var information = json.paths[0].instructions;

    for(var i in information) {
        var step = information[i].text;
        $('#directionList').append('<li class="hereugo">' + step + '</li>');
    }
};