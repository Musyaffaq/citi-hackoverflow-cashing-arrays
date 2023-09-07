/*!

=========================================================
* Black Dashboard React v1.2.2
=========================================================

* Product Page: https://www.creative-tim.com/product/black-dashboard-react
* Copyright 2023 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/black-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
// nodejs library that concatenates classes
import classNames from "classnames";
// react plugin used to create charts
import { Line, Bar } from "react-chartjs-2";

// reactstrap components
import {
  Button,
  ButtonGroup,
  Card,
  CardHeader,
  CardBody,
  CardTitle,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  UncontrolledDropdown,
  Label,
  FormGroup,
  Input,
  Table,
  Row,
  Col,
} from "reactstrap";

// core components
import {
  chartExample1,
  chartExample2,
  chartExample3,
  chartExample4,
} from "variables/charts.js";

// ViewChart Widget;
import TradingViewWidget from "./ViewChart.js";
import TradingViewSymbol from "./HeaderInfo.js";
import TradingViewNews from "./News.js";

function Dashboard(props) {
  const [bigChartData, setbigChartData] = React.useState("data1");
  console.log("received: " + props.name);
  const setBgChartData = (name) => {
    setbigChartData(name);
  };

  const handleTitleClick = (url) => {
    window.open(url, "_blank");
  };
  return (
    <>
      <div className="content">
        {/* Symbol */}
        <Row>
          <Col xs="12">
            <Card className="card" display="flex">
              <TradingViewSymbol name={props.name} />
            </Card>
          </Col>
        </Row>

        <Row>
          <Col md="5">
            <Card className="card-tasks">
              <CardHeader>
                <CardTitle tag="h2">Insights</CardTitle>
              </CardHeader>

              <CardBody>
                <div className="insight table-full-width table-responsive insights">
                  <Table>
                    <tbody>
                      <tr>
                        <td>
                          <p>{props.info.insight}</p>
                        </td>
                      </tr>
                    </tbody>
                  </Table>
                </div>
              </CardBody>
            </Card>

            <Row>
              <Col lg="6">
                <Card className="card-chart">
                  <CardHeader>
                    <h5 className="card-category">Confidence Score</h5>
                    <CardTitle tag="h3">
                      <i className="tim-icons icon-send text-success" />{" "}
                      {props.info.prediction.r2.toFixed(2) * 100}%
                    </CardTitle>
                  </CardHeader>
                  <CardBody>
                    {/* <div className="chart-area">
                      <Line
                        data={chartExample2.data}
                        options={chartExample2.options}
                      />
                    </div> */}
                  </CardBody>
                </Card>
              </Col>

              <Col lg="6">
                <Card className="card-chart">
                  <CardHeader>
                    <h5 className="card-category">Predicted Direction</h5>
                    <CardTitle tag="h3">
                      {/* <i className="tim-icons icon-minimal-up text-success" /> Up */}
                      {/* <i className="tim-icons icon-minimal-down text-warning" />{" "} */}
                      ${props.info.prediction.predicted_price.toFixed(2)}
                    </CardTitle>
                  </CardHeader>
                  <CardBody></CardBody>
                </Card>
              </Col>
            </Row>
          </Col>

          <Col md="7">
            {/* <Card className="card-chart " display="flex">
                  <CardHeader>
                    <h5 className="card-category">Total Shipments</h5>
                    <CardTitle tag="h3">
                      <i className="tim-icons icon-bell-55 text-info" /> 763,215
                    </CardTitle>
                  </CardHeader>
                  <CardBody>
                    <div className="chart-area">
                      <Line
                        data={chartExample2.data}
                        options={chartExample2.options}
                      />
                    </div>
                  </CardBody>
                </Card> */}

            <Card>
              <CardHeader>
                <CardTitle tag="h4">Insights Sources</CardTitle>
              </CardHeader>
              <CardBody>
                <Table className="tablesorter " responsive>
                  <div className="articles">
                    <tbody>
                      {props.info.articles.map((article, index) => (
                        <tr key={index}>
                          <td>
                            <p
                              className="title clickable-title"
                              onClick={() => handleTitleClick(article.url)}
                            >
                              {article.title}
                            </p>
                            {/* <p>{article.description}</p> */}
                            <p className="text-muted">{article.date}</p>
                            {article.tags.split(",").map((tag, tagIndex) => (
                              <span
                                key={tagIndex}
                                className="badge badge-primary"
                              >
                                {tag}
                              </span>
                            ))}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </div>
                </Table>
              </CardBody>
            </Card>
          </Col>
        </Row>

        {/* *****************Large Chart Here***************** */}
        <Row>
          <Col xs="12">
            <Card className="card">
              <TradingViewWidget name={props.name} />
            </Card>
          </Col>
        </Row>

        <Row>
          <Col xs="12">
            <Card className="card" display="flex">
              <TradingViewNews name={props.name} />
            </Card>
          </Col>
        </Row>
      </div>
    </>
  );
}

export default Dashboard;
