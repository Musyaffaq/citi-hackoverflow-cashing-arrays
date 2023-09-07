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
  UncontrolledTooltip,
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
  console.log("received: "+ props.name);
  const setBgChartData = (name) => {
    setbigChartData(name);
  };
  return (
    <>
      <div className="content">

        {/* <Row>
          <Col lg="12">
            <div>
              <TradingViewSymbol/>
            </div>
          </Col>
        </Row> */}

        {/* Symbol */}
        <Row>
          <Col xs="12">
            <Card className="card" display="flex">
            <TradingViewSymbol name={props.name}/>
            </Card>
          </Col>
        </Row>

        <Row>
          <Col lg="6" md="8">


          
            <Card className="card-tasks">
            <CardHeader>
                {/* <h5 className="card-category">Stock Performance</h5> */}
                    <CardTitle tag="h2">Insights</CardTitle>
              </CardHeader>
              
              <CardBody>
                <div className="table-full-width table-responsive">
                  <Table>
                    <tbody>
                      <tr>
                        <td>
                          <p className="title">Update the Documentation</p>
                          <p className="text-muted">
                            Dwuamish Head, Seattle, WA 8:47 AM
                          </p>
                        </td>
                      </tr>

                      <tr>
                        <td>
                          <p className="title">GDPR Compliance</p>
                          <p className="text-muted">
                            The GDPR is a regulation that requires businesses to
                            protect the personal data and privacy of Europe
                            citizens for transactions that occur within EU
                            member states.
                          </p>
                        </td>
                      </tr>


                      <tr>
                        <td>
                          <p className="title">Solve the issues</p>
                          <p className="text-muted">
                            Fifty percent of all respondents said they would be
                            more likely to shop at a company
                          </p>
                        </td>
                      </tr>

                      <tr>
                        <td>
                          <p className="title">Release v2.0.0</p>
                          <p className="text-muted">
                            Ra Ave SW, Seattle, WA 98116, SUA 11:19 AM
                          </p>
                        </td>
                      </tr>


                      <tr>
                        <td>
                          <p className="title">Export the processed files</p>
                          <p className="text-muted">
                            The report also shows that consumers will not easily
                            forgive a company once a breach exposing their
                            personal data occurs.
                          </p>
                        </td>
                      </tr>


                      <tr>
                        <td>
                          <p className="title">Arival at export process</p>
                          <p className="text-muted">
                            Capitol Hill, Seattle, WA 12:34 AM
                          </p>
                        </td>
                      </tr>
                    </tbody>
                  </Table>
                </div>
              </CardBody>
            </Card>
        
          </Col>


          

          <Col lg="6" md="4">


            <Row>
              <Col lg="6">
                <Card className="card-chart" >
                  <CardHeader>
                    <h5 className="card-category">Confidence Score</h5>
                    <CardTitle tag="h3">
                      <i className="tim-icons icon-send text-success" /> 89.5%
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
                <Card className="card-chart" >
                  <CardHeader>
                    <h5 className="card-category">Predicted Direction</h5>
                    <CardTitle tag="h3">
                      {/* <i className="tim-icons icon-minimal-up text-success" /> Up */}
                      <i className="tim-icons icon-minimal-down text-warning" /> Down
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
            </Row>

            <Card className="card-chart " display="flex">
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
                </Card>

          </Col>



          {/* <Col lg="3">
            <Card className="card-chart"> 
              <CardHeader>
                <h5 className="card-category">Daily Sales</h5>
                <CardTitle tag="h3">
                  <i className="tim-icons icon-delivery-fast text-primary" />{" "}
                  3,500€
                </CardTitle>
              </CardHeader>
              <CardBody>
                <div className="chart-area">
                  <Bar
                    data={chartExample3.data}
                    options={chartExample3.options}
                  />
                </div>
              </CardBody>
            </Card>
          </Col> */}

        </Row>

        {/* <Row>
            <TradingViewWidget/>
        </Row> */}


{/* *****************Large Chart Here***************** */}
          <Row>
          <Col xs="12">
            <Card className="card">
            <TradingViewWidget name={props.name}/>
            </Card>
          </Col>
        </Row>


        <Row>
          <Col xs="12">
            <Card className="card" display="flex">
            <TradingViewNews name={props.name}/>
            </Card>
          </Col>
        </Row>



        





        
      </div>
    </>
  );
}

export default Dashboard;
