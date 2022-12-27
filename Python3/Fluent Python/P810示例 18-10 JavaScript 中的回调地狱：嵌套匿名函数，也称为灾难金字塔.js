api_call(request1, function (response1) {
    // 第一步
    var request2 = step1(response1);

    api_call2(request2, function (response2) {
        // 第二步
        var request3 = step2(response2);

        api_call3(request3, function(response3) {
            // 第三步
            step3(response3);
        });
    });
});

console.log(api_call())