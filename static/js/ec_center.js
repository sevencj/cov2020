var ec_center = echarts.init(document.getElementById('c2'))

var mydata = [{'name':'上海', 'value': 318}, {'name':'云南', 'value': 162}]

var ec_center_option = {
    title: {
        text: '',
		left: 'center',
		textStyle:{
			color:'white',
            fontSize: 30,
		},
    },
	tooltip: {
		trigger:'item'
	},
	visualMap: {
		show:true,
		x:'left',
		y:'bottom',
		textStyle:{
			fontSize:15,
			color:'white',
		},
		splitList: [{start:1, end:0},
		    {start:10, end:99},
			{start:100, end:999},
			{start:1000, end:9999},
			{start:10000}],
		color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
	},
	series: [{
		name:'累计确诊人数',
		type:'map',
		mapType:'china',
		roam:false,
		itemStyle: {
			normal: {
				borderwidth:.5,
				borderColor:'#009fe8',
				areaColor:'#ffefd5',
			},
			emphasis: {
				borderwidth:.5,
				borderColor:'#4b0082',
				areaColor:'#fff',
			}
		},
		lable: {
			normal: {
				show:true, //省份名称
				fontSize:8,
			},
			emphasis: {
				show:true,
				fontSize:8,
			}
		},
		data: mydata   //mydata
	}]
};
ec_center.setOption(ec_center_option)