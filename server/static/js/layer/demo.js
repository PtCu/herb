function ShowText() {
    layer.open({
        type: 1,
        title: "关联新设备",
        area: ["395px", "300px"],
        content: $("#loginBox"),
    });
}


function fixSubmit() {
    var fixPhone = $.trim($("#fixPhone").val());
    var fixAddress = $.trim($("#fixAddress").val());
    var fixDescribe = $.trim($("#fixDescribe").val());
    if (fixPhone == "" || fixAddress == "" || fixDescribe == "") {
        layer.alert("内容不能为空，请输入", {
            title: "提示",
            icon: 5,
        });
        return false;
    } else {
        layer.alert("提交成功，工作人员将在1-2个工作日内与您联系", {
            title: "提示",
            icon: 6,
        });
    }
}


function cancel() {
    // var url=$.trim($("#disUrl").val());
    layer.confirm(
        "是否确认取消关联",
        {btn: ['确认', '取消']},
        function () {
            layer.msg('已取消关联', {icon: 1});
            return false;
        },
        function () {
            layer.msg('取消关联', {icon: 2})
            return true;
        }
    )
}