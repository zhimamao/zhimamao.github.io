const Service = require('node-windows').Service;

const svc = new Service({
	name: 'unblock-netease-cloud-music',
	description: '点亮网易云音乐灰色歌曲',
	script: './app.js', // 入口文件路径
	// scriptOptions:'-p 52100:52101', // 可选参数示例: 自定义端口并开启HTTPS
	wait: '1', // 程序崩溃后重启时间间隔
	grow: '0.25', // 重启等待时间成长值，第一次1秒，第二次1.25秒。。。
	maxRestarts: '40', // 60秒内最大重启次数
});

// 监听
svc.on('install', () => {
	svc.start();
	console.log('Installation completed.');
});
svc.on('uninstall', () => console.log('Uninstallation completed.'));

// 卸载
if (svc.exists) return svc.uninstall();

// 安装
svc.install();
