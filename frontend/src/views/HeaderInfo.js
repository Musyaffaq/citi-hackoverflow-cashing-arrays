// import React, { useEffect, useRef, memo } from 'react';

// function TradingViewSymbol() {
//   const container = useRef();

//   useEffect(() => {
//     const script = document.createElement('script');
//     script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js';
//     script.type = 'text/javascript';
//     script.async = true;
//     script.innerHTML = `
//       {
//         "symbol": "NASDAQ:AAPL",
//         "width": "100%",
//         "locale": "en",
//         "colorTheme": "dark",
//         "isTransparent": true
//       }
//     `;
//     container.current.appendChild(script);

//     return () => {
//       // Clean up by removing the script when the component unmounts
//       container.current.removeChild(script);
//     };
//   }, []);

//   return (
//     <div className="tradingview-widget-container" ref={container}>
//       <div className="tradingview-widget-container__widget"></div>
//     </div>
//   );
// }

// export default memo(TradingViewSymbol);


import React, { useEffect, useRef, memo, useState } from "react";
// import symbol from "components/Navbars/AdminNavbar";

function TradingViewSymbol(props) {
  const container = useRef();
  // console.log("headerinfo: " + props.name);
  // // const [symbol, setSymbol] = useState("NASDAQ:AAPL"); // Initial symbol
  // console.log(container.current);

  useEffect(() => {
    const script = document.createElement("script");
    script.src =
      "https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js";
    script.type = "text/javascript";
    script.async = true;
    script.id = "1";
    script.innerHTML = JSON.stringify({
      symbol: props.name, // Use the symbol from state
      width: "100%",
      locale: "en",
      colorTheme: "dark",
      isTransparent: true,
    });
    // if (props.name !== "")
    container.current.appendChild(script);

    return () => {
      // Clean up by removing the script when the component unmounts
      
      // container.current.removeChild(container.current.children[0]);


      // if (container.current.contains(script)) {
        container.current.removeChild(container.current.children[0]);
        container.current.removeChild(container.current.children[0]);
      // }
      console.log("rerunned yay");
      // console.log(container.current);

    };
  }, [props.name]); // Re-run the effect whenever the symbol changes

  return (
    <div className="tradingview-widget-container" ref={container}>
      <div className="tradingview-widget-container__widget"></div>
    </div>
  );
}

export default memo(TradingViewSymbol);
