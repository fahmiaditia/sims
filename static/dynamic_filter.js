var send_data = {}

		$(document).ready(function (){
			resetFilters();
			getAPIData();
			getKelas_data();
			getTahun_Ajaran_data();
			getSemester_data();
			getKD_data();

			$('#kelas').on('change', function () {
		        // since province and region is dependent 

		        // on country select, emty all the options from select input

		        $("#semester").val("all");
		        $("#tahun_ajaran").val("all");
		        $("#kd").val("all");
		        send_data['semester'] = '';
		        send_data['tahun_ajaran'] = '';
		        send_data['kd'] = '';

		        // update the selected country

		        if(this.value == "all")
		            send_data['kelas'] = "";
		        else
		            send_data['kelas'] = this.value;

		        //get province of selected country

		        getKelas_data(this.value);
		        // get api data of updated filters

		        getAPIData();
		    });

		})

		
		function resetFilters(){
			$('#kelas').val('all');
			$('#tahun_ajaran').val('all');
			$('#semester').val('all');
			$('#kd').val('all');
			// $('display_all').val('none');

			send_data['kelas'] = '';
			send_data['tahun_ajaran'] = '';
			send_data['semester'] = '';
			send_data['kd'] = '';

		}

		function putTableData(result) {
		    // creating table row for each result and

		    // pushing to the html cntent of table body of listing table

		    let row;
		    if(result["results"].length > 0){
		        $("#no_results").hide();
		        $("#list_data").show();
		        $("#listing").html("");  
		        $.each(result["results"], function (a, b) {
		            row = "<tr> <td>" + b.kelas + "</td>" +
		                "<td>" + b.tahun_ajaran_nilai_toogle + "</td>" +
		                "<td>" + b.semester_toogle + "</td>" +
		                "<td>" + b.kd_toogle + "</td>" +
		                "<td>" + b.penilaian_ke_toogle + "</td>" +
		                "<td>" + b.nilai_P1_TGS_toogle + "</td>" +
		                "<td>" + b.nilai_P2_TLS_toogle + "</td>" +
		                "<td>" + b.nilai_P3_TLS_toogle + "</td></tr>"
		            $("#listing").append(row);   
		        });
		    }
		    else{
		        // if no result found for the given filter, then display no result

		        $("#no_results h5").html("No results found");
		        $("#list_data").hide();
		        $("#no_results").show();
		    }
		    // setting previous and next page url for the given result

		    let prev_url = result["previous"];
		    let next_url = result["next"];
		    // disabling-enabling button depending on existence of next/prev page. 

		    if (prev_url === null) {
		        $("#previous").addClass("disabled");
		        $("#previous").prop('disabled', true);
		    } else {
		        $("#previous").removeClass("disabled");
		        $("#previous").prop('disabled', false);
		    }
		    if (next_url === null) {
		        $("#next").addClass("disabled");
		        $("#next").prop('disabled', true);
		    } else {
		        $("#next").removeClass("disabled");
		        $("#next").prop('disabled', false);
		    }
		    // setting the url

		    $("#previous").attr("url", result["previous"]);
		    $("#next").attr("url", result["next"]);
		    // displaying result count

		    $("#result-count span").html(result["count"]);
		}

		function getAPIData(){
			let url = $('#list_data').attr('url')
			$.ajax({
				method: "GET",
				url: url,
				data: send_data,
				beforeSend: function(){
					$("#no_result h5").html("Loading data..");
				},
				success: function(result){
					putTableData(result);
				},
				error: function(response){
					$("#no_result h5").html("Something wrong");
					$("#list_data").hide();
				}
			});
		}

		function getKelas_data(){
			let url = $("#kelas").attr("url");

			$.ajax({
				method: "GET",
				url: url,
				data: {},
				success: function(result){
					kelas_option = "<option value='all' selected>Semua Kelas</option>";
					$.each(result["kelas"], function(a, b){
						kelas_option += "<option>" + b + "</option>"
					});
					$("#kelas").html(kelas_option)
				},
				error: function(response){
					console.log(response)
				}
			})
		}

		function getTahun_Ajaran_data(){
			let url = $("#tahun_ajaran").attr("url");

			$.ajax({
				method: "GET",
				url: url,
				data: {},
				success: function(result){
					tahun_ajaran_option = "<option value='all' selected>Semua Tahun Ajaran</option>";
					$.each(result['tahun_ajaran'], function(a, b){
						tahun_ajaran_option += "<option>" + b + "</option>"
					});
					$("#tahun_ajaran").html(tahun_ajaran_option)
				},
				error: function(response){
					console.log(response)
				}
			})
		}

		function getSemester_data(){
			let url = $("#semester").attr("url");

			$.ajax({
				method: "GET",
				url: url,
				data: {},
				success: function(result){
					semester_option = "<option value='all' selected>Semua Semester</option>";
					$.each(result['semester'], function(a, b){
						semester_option += "<option>" + b + "</option>"
					});
					$("#semester").html(semester_option)
				},
				error: function(response){
					console.log(response)
				}
			})
		}

		function getKD_data(){
			let url = $("#kd").attr("url");

			$.ajax({
				method: "GET",
				url: url,
				data: {},
				success: function(result){
					kd_option = "<option value='all' selected>Semua KD</option>";
					$.each(result['kd'], function(a, b){
						kd_option += "<option>" + b + "</option>"
					});
					$("#kd").html(kd_option)
				},
				error: function(response){
					console.log(response)
				}
			})
		}