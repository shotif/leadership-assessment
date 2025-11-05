(() => {
    const config = window.leadershipData;
    if (!config) {
        return;
    }

    const buildRadarDataset = (assessment) => {
        const scores = config.dimensionKeys.map((key) => assessment.dimensions[key]);
        return {
            labels: config.dimensionLabels,
            datasets: [
                {
                    label: assessment.full_name,
                    data: scores,
                    fill: true,
                    backgroundColor: 'rgba(13, 110, 253, 0.2)',
                    borderColor: 'rgba(13, 110, 253, 1)',
                    pointBackgroundColor: 'rgba(13, 110, 253, 1)'
                }
            ]
        };
    };

    const renderMatrix = async () => {
        const response = await fetch('/api/assessments');
        if (!response.ok) {
            return;
        }
        const assessments = await response.json();
        const ctx = document.getElementById('matrixChart');
        if (!ctx) {
            return;
        }
        const data = {
            datasets: [
                {
                    label: 'Procjene',
                    data: assessments.map((assessment) => ({
                        x: assessment.adequacy,
                        y: assessment.potential,
                        name: assessment.full_name,
                        category: assessment.category
                    })),
                    backgroundColor: 'rgba(25, 135, 84, 0.7)'
                }
            ]
        };
        new Chart(ctx, {
            type: 'scatter',
            data,
            options: {
                plugins: {
                    tooltip: {
                        callbacks: {
                            label(context) {
                                const { raw } = context;
                                return `${raw.name} (Adekv.: ${raw.x}, Potenc.: ${raw.y}) - ${raw.category}`;
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        suggestedMin: 1,
                        suggestedMax: 5,
                        title: { display: true, text: 'Adekvatnost' }
                    },
                    y: {
                        suggestedMin: 1,
                        suggestedMax: 5,
                        title: { display: true, text: 'Potencijal' }
                    }
                }
            }
        });
    };

    const renderIndividual = async () => {
        if (!config.selectedId) {
            return;
        }
        const response = await fetch(`/api/assessments/${config.selectedId}`);
        if (!response.ok) {
            return;
        }
        const assessment = await response.json();
        const ctx = document.getElementById('individualChart');
        if (!ctx) {
            return;
        }
        new Chart(ctx, {
            type: 'radar',
            data: buildRadarDataset(assessment),
            options: {
                scales: {
                    r: {
                        suggestedMin: 1,
                        suggestedMax: 5,
                        ticks: {
                            stepSize: 1
                        }
                    }
                }
            }
        });

        const insightButton = document.getElementById('generateInsight');
        if (insightButton) {
            insightButton.addEventListener('click', async () => {
                const output = document.getElementById('insightOutput');
                if (!output) {
                    return;
                }
                output.textContent = 'Generiranje u tijeku...';
                try {
                    const response = await fetch(`/api/insights/${config.selectedId}`);
                    const payload = await response.json();
                    if (!response.ok) {
                        output.textContent = payload.error || 'Generiranje nije uspjelo.';
                        return;
                    }
                    output.textContent = payload.content;
                } catch (error) {
                    output.textContent = 'Došlo je do pogreške pri pozivu usluge.';
                }
            });
        }
    };

    const renderComparison = async () => {
        const chartConfigs = [
            { id: config.comparisonA, canvasId: 'comparisonChartA' },
            { id: config.comparisonB, canvasId: 'comparisonChartB' }
        ];
        for (const entry of chartConfigs) {
            if (!entry.id) {
                continue;
            }
            const response = await fetch(`/api/assessments/${entry.id}`);
            if (!response.ok) {
                continue;
            }
            const assessment = await response.json();
            const ctx = document.getElementById(entry.canvasId);
            if (!ctx) {
                continue;
            }
            new Chart(ctx, {
                type: 'radar',
                data: buildRadarDataset(assessment),
                options: {
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        r: {
                            suggestedMin: 1,
                            suggestedMax: 5,
                            ticks: { stepSize: 1 }
                        }
                    }
                }
            });
        }
    };

    switch (config.mode) {
        case 'matrix':
            renderMatrix();
            break;
        case 'individual':
            renderIndividual();
            break;
        case 'comparison':
            renderComparison();
            break;
        default:
            break;
    }
})();
