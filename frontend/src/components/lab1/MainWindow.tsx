import {
    Button,
    Container,
    Title,
    Divider,
    Group,
    Space,
    Radio,
    RadioGroup,
    Table,
} from "@mantine/core";
import { MainWindowProps } from "../../types/types";

const exampleSortingResults = [
    {
        algorithm: "SortDirectInclusion (n²)",
        times: {
            "10 000": "1.184263",
            "100 000": "120.69563221931458",
            "500 000": "603.478161097",
        },
    },
    {
        algorithm: "SortDirectSelection (n²)",
        times: {
            "10 000": "1.556144",
            "100 000": "156.65176558494568",
            "500 000": "783.258827925",
        },
    },
    {
        algorithm: "SortDirectExchange (n²)",
        times: {
            "10 000": "4.001043",
            "100 000": "401.85486793518066",
            "500 000": "2009.27433968",
        },
    },
    {
        algorithm: "QuickSort (n log n)",
        times: {
            "10 000": "0.001278",
            "100 000": "0.012976408004760742",
            "500 000": "0.06488204002",
        },
    },
    {
        algorithm: "ShellSort (n log² n)",
        times: {
            "10 000": "0.010780",
            "100 000": "0.13507890701293945",
            "500 000": "0.67539453506",
        },
    },
];

export const MainWindow: React.FC<MainWindowProps> = ({
    sortingResults,
    loading,
    sortPercent,
    setSortPercent,
    sortMassive,
    setSortMassive,
    fetchSortingResults,
}) => {
    const minTime = Math.min(...sortingResults.map((result) => result.time));
    const maxTime = Math.max(...sortingResults.map((result) => result.time));

    return (
        <Container my="xl">
            <Title order={2} mb="xl">
                Лаб. работа №1
            </Title>
            <Divider
                my="sm"
                label="Размер массива"
                labelPosition="center"
            />
            <RadioGroup size="md" value={sortMassive} onChange={setSortMassive}>
                <Group gap={"xl"} justify="center">
                    {["1000", "5000", "7000", "10000"].map((massive) => (
                        <Radio key={massive} value={massive} label={massive} />
                    ))}
                </Group>
            </RadioGroup>
            <Space h="xl" />
            <Divider
                my="sm"
                label="Степень отсортированности массива"
                labelPosition="center"
            />
            <RadioGroup size="md" value={sortPercent} onChange={setSortPercent}>
                <Group gap={"xl"} justify="center">
                    {["0%", "25%", "50%", "75%", "100%"].map((percent) => (
                        <Radio key={percent} value={percent} label={percent} />
                    ))}
                </Group>
            </RadioGroup>
            <Space h="xl" />
            <Divider my="sm" label="Результат" labelPosition="center" />

            <Table>
                <thead>
                    <tr>
                        <th style={{ textAlign: "center" }}>Алгоритм</th>
                        <th style={{ textAlign: "center" }}>
                            Время выполнения (сек)
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {loading ? (
                        <tr>
                            <td colSpan={2} style={{ textAlign: "center" }}>
                                Загрузка...
                            </td>
                        </tr>
                    ) : sortingResults.length > 0 ? (
                        sortingResults.map((result) => (
                            <tr key={result.name}>
                                <td style={{ textAlign: "center" }}>
                                    {result.name}
                                </td>
                                <td
                                    style={{
                                        textAlign: "center",
                                        color:
                                            result.time === minTime
                                                ? "green"
                                                : result.time === maxTime
                                                ? "red"
                                                : "white",
                                    }}
                                >
                                    {result.time.toFixed(6)}
                                </td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan={2} style={{ textAlign: "center" }}>
                                Данных нет
                            </td>
                        </tr>
                    )}
                </tbody>
            </Table>

            <Group mt="lg" justify="center">
                <Button
                    radius="xl"
                    size="md"
                    onClick={fetchSortingResults}
                    disabled={loading}
                >
                    Посчитать
                </Button>
            </Group>
            <Space h="xl" />

            <Divider my="sm" label="Пример результата" labelPosition="center" />
            <Table>
                <thead>
                    <tr>
                        <th style={{ textAlign: "center" }}>Алгоритм</th>
                        <th style={{ textAlign: "center" }}>
                            10 000 элементов
                        </th>
                        <th style={{ textAlign: "center" }}>
                            100 000 элементов
                        </th>
                        <th style={{ textAlign: "center" }}>
                            500 000 элементов
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {exampleSortingResults.map((result) => (
                        <tr key={result.algorithm}>
                            <td style={{ textAlign: "center" }}>
                                {result.algorithm}
                            </td>
                            <td style={{ textAlign: "center" }}>
                                {result.times["10 000"]}
                            </td>
                            <td style={{ textAlign: "center" }}>
                                {result.times["100 000"]}
                            </td>
                            <td style={{ textAlign: "center" }}>
                                {result.times["500 000"]}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </Container>
    );
};
