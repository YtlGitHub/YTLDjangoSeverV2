//自定义执行信息删除提示判断，参数uu是成功的删除url地址
function doDel(uu){
  if (confirm("确定要删除？!!!")){
	//网页跳转
	window.location=uu;
  }
}

//<button></button>
function doDel2(url){
  Modal.confirm({
	msg: "确定要删除吗？",
	title: "信息提示",
	btnok: "确定",
	btbcl: "取消",
  }).on(function (e){
	if(e){
	  window.location.href=url;
	}
	})
}

//延时5秒弹框
function timedMsg()
{
var t=setTimeout("alert('5 seconds!')",5000)
}
//onClick="timedMsg()"inout、button加这个调用延时5秒弹框

//报警提示弹框：onclick="display_alert()"
function display_alert()
  {
  alert("我是一个警报箱！！")
  alert("再打个招呼。这里演示了" + "\n" + "如何在消息框中添加折行。")
  }

//confirm() 方法用于显示一个带有指定消息和 OK 及取消按钮的对话框。onclick="disp_confirm()"
function disp_confirm()
  {
  var r=confirm("按下按钮")
  if (r==true)
    {
    document.write("你按了确认键！")
    }
  else
    {
    document.write("你按了取消键！")
    }
  }

//将以 JSON 格式编写的字符串转换为 Javascript 对象<p id="demo"></p>
var myJSON = '{ "name":"Bill", "age":19, "city":"Seattle" }';
var myObj = JSON.parse(myJSON);
document.getElementById("demo").innerHTML = myObj.name;

//提示弹框，JavaScript脚本触发弹框：$("#myModal").modal()
$("#myBtn").click(function(){
  //显示modal
  $("myModal").modal();
});
//点击确定删除按钮，隐藏modal
$(".modal-footer>.btn-primary").click(function(){
  //执行一些事情
  //模态框modal收回去
  $("#myModal").modal('hide');
});

//提交数据函数
function add_smoke() {
	$.ajax({
	//几个参数需要注意一下
		cache:false,
		type: "POST",//方法类型
		dataType: "json",//预期服务器返回的数据类型
		url: "/myadmin/user/1/" ,//url
		data: $('#add-smoke-form').serialize(), //将模态框的form表单数据序列化，以便提交到后台
		async:false,  //必须要为false,必须必须

		success: function (data) {
			console.log(data);//打印服务端返回的数据(调试用)
			if(data.status == "success"){

				//关闭模态框并清除框内数据，否则下次打开还是上次的数据
				document.getElementById("add-smoke-form").reset();
				$('#myModal').modal('hide');

				//判断确实正确入库之后提示#}
				toastr.success('提交数据成功');

				//刷新表格数据#}
				$("#mytab").bootstrapTable('refresh');

			 }
		 },
		error : function() {
			toastr.warning("请输入所有数据");
		 }
	});
}


// 显示搜索打印excel
$(function () {
  $("#example1").DataTable({
	"responsive": true, "lengthChange": false, "autoWidth": false,
	"buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
  }).buttons().container().appendTo('#example1_wrapper .col-md-6:eq(0)');
  $('#example2').DataTable({
	"paging": true,
	"lengthChange": false,
	"searching": false,
	"ordering": true,
	"info": true,
	"autoWidth": false,
	"responsive": true,
  });
});