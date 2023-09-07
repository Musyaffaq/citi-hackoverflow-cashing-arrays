import React, { useEffect, useRef, memo } from 'react';

function TradingViewNews(props) {
  const container = useRef();

  useEffect(() => {
    const script = document.createElement('script');
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-timeline.js';
    script.type = 'text/javascript';
    script.async = true;
    script.innerHTML = JSON.stringify({
      feedMode: "symbol",
      symbol: props.name,
      colorTheme: "dark",
      isTransparent: true,
      displayMode: "regular",
      width: "100%",
      height: "500",
      locale: "en"
    });
    container.current.appendChild(script);

    return () => {
      // Clean up by removing the script when the component unmounts
      container.current.removeChild(container.current.children[0]);
      container.current.removeChild(container.current.children[0]);
    };
  }, [props.name]);

  return (
    <div className="tradingview-widget-container" ref={container}>
      <div className="tradingview-widget-container__widget"></div>
    </div>
  );
}

export default memo(TradingViewNews);
