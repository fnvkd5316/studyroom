(function() {
  let initData = {
    coords: [{latitude: null, longitude: null}]
  }
  const mapContainer = document.getElementById("map"), // 지도를 표시할 div
        mapOption = {
          center: new kakao.maps.LatLng(37.56682, 126.97865), // 지도의 중심좌표
          level: 5, // 지도의 확대 레벨
          mapTypeId: kakao.maps.MapTypeId.ROADMAP, // 지도종류
        };

  // 지도를 생성한다
  const map = new kakao.maps.Map(mapContainer, mapOption);

  // 지도에 마커와 인포윈도우(말풍선)를 표시하는 함수입니다
  function displayMarker(locPosition, message) {
    const { latitude, longitude } = locPosition;
    initData.coords = [{latitude: latitude, longitude: longitude}]
    const position = new kakao.maps.LatLng(latitude, longitude); // 지도의 중심좌표
    // 마커를 생성합니다
    const marker = new kakao.maps.Marker({
      map: map,
      position: position, // 현재위치의 마커 입니다.!!
    });

    // 커스텀 오버레이를 생성합니다
    new kakao.maps.CustomOverlay({
      map: map,
      position: position,  // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
      content: message,
      yAnchor: 1,
    });

    // 마커가 지도 위에 표시되도록 설정합니다
    marker.setMap(map)
    // 지도 중심좌표를 접속위치로 변경합니다
    map.setCenter(position);
  }

  // geolocation true 기능 //
  function geolocationT(){
    // GeoLocation을 이용해서 접속 위치를 얻어옵니다
    navigator.geolocation.getCurrentPosition(function (position) {
    const message = `<div class="customMarker">
                  <div class="info">지금 여기에 계십니다.!!</div>
                  </div>
                `; // 인포윈도우에 표시될 내용입니다

      // 마커와 인포윈도우를 표시합니다
      displayMarker(position.coords, message);
    });
  };
  // geolocation true 기능 //
  // geolocation false 인경우 기능 //
  function geolocationF(){
    const locPosition = new kakao.maps.LatLng(33.450701, 126.570667),
      message = "geolocation을 사용할수 없어요..";

    displayMarker(locPosition, message);
  };
  // geolocation false 인경우 기능 //

  const base_url = "/map";
  async function getData() {
    const res = await fetch(base_url);
    return res.text();
  };

  async function init() {
    const db = JSON.parse(await getData());
    // HTML5의 geolocation으로 사용할 수 있는지 확인합니다
    if (navigator.geolocation) {
      geolocationT();
    } else {
      // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다
      geolocationF();
    }

    // data.json있는 데이터 불러와 뿌려준다. //
    db.datas.forEach((item) => {
      const { name, positions } = item;

      // 커스텀 오버레이에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
      const temp_html = `<div class="customoverlay">
                        <a href="https://map.kakao.com/link/map/${name},${positions[0]},${positions[1]}"" target="_blank">
                            <span class="title">${name}</span>
                        </a></div>`;

      // 커스텀 오버레이를 생성합니다
      const marker = new kakao.maps.CustomOverlay({
        map: map,
        position: new kakao.maps.LatLng(positions[0], positions[1]),
        content: temp_html,
        yAnchor: 1,
      });

      // 마커가 지도 위에 표시되도록 설정합니다.
      marker.setMap(map);
    });
    // data.json있는 데이터 불러와 뿌려준다. //
  };
  
  function showMap(e) {
    const self = $(e.currentTarget);
    const i = self.children('i');
    if(i.hasClass('ic-map')){
      self.addClass('on')
      i.removeClass();
      i.addClass('ic-menu');
      $('.mapShow').text('목록보기');
      $('.card_wrap').hide()
      $('.map_wrap').show()
      map.relayout()
      map.setCenter(new kakao.maps.LatLng(initData.coords[0].latitude, initData.coords[0].longitude));
    } else {
      self.removeClass('on')
      i.addClass('ic-map');
      $('.mapShow').text('지도보기');
      $('.card_wrap').show()
      $('.map_wrap').hide()
    }
  };

  init();
  $('.btn-js').on('click', showMap);
})();
